import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

# Load environment variables from the .env file
# (The .env file lives in the secrets/ folder)
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "secrets", ".env")
load_dotenv(dotenv_path)

# Get the path to the Firebase key file
cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# Connect to Firestore
cred = credentials.Certificate(cred_path)
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)
db = firestore.client()

# ---------------- CRUD FUNCTIONS ---------------- #

def add_habit(user_id, habit_name, target_per_week):
    """Add a new habit to Firestore."""
    habit_ref = db.collection("habits").document()  # auto-generated ID
    habit_ref.set({
        "user_id": user_id,
        "habit_name": habit_name,
        "target_per_week": target_per_week,
        "completed_times": 0,
        "last_updated": datetime.now()
    })
    print(f"\nSuccessfully added habit: {habit_name}")


def print_habits(user_id):
    print("\nYour Habits:")
    habits = db.collection("habits").where("user_id", "==", user_id).stream()
    for doc in habits:
        data = doc.to_dict()
        print(f"""ID: {doc.id}\nHabit: {data['habit_name']}\nTarget per week: {data['target_per_week']}\nCompleted: {data['completed_times']}\nLast updated: {data['last_updated']}""")
        print("----------------------------\n")

def update_habit(habit_id, updates):
    """Update a habit by its document ID."""
    db.collection("habits").document(habit_id).update(updates)
    print("\nHabit updated successfully.")


def delete_habit(habit_id):
    """Delete a habit by its document ID."""
    db.collection("habits").document(habit_id).delete()
    print("\nHabit deleted successfully.")

def log_completion(habit_id):
    """Increment completed_times and update timestamp."""
    doc_ref = db.collection("habits").document(habit_id)
    doc = doc_ref.get()
    if doc.exists:
        data = doc.to_dict()
        new_count = data.get("completed_times", 0) + 1
        doc_ref.update({
            "completed_times": new_count,
            "last_updated": datetime.now()
        })
        print(f"\nHabit progress updated! Total completions: {new_count}")
    else:
        print("Habit not found.")
