import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

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
        "target_per_week": target_per_week
    })
    print(f"✅ Added habit: {habit_name}")


def print_habits(user_id):
    """Retrieve and display all habits for a user."""
    print("\n📋 Your Habits:")
    habits = db.collection("habits").where("user_id", "==", user_id).stream()
    for doc in habits:
        data = doc.to_dict()
        print(f"ID: {doc.id} | {data['habit_name']} - {data['target_per_week']} times/week")


def update_habit(habit_id, updates):
    """Update a habit by its document ID."""
    db.collection("habits").document(habit_id).update(updates)
    print("✏️ Habit updated successfully.")


def delete_habit(habit_id):
    """Delete a habit by its document ID."""
    db.collection("habits").document(habit_id).delete()
    print("🗑️ Habit deleted successfully.")

