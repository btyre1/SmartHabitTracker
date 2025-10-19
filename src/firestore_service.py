# AI helped with debugging this file
import os
from dotenv import load_dotenv  # AI used to explain this import 
import firebase_admin
from firebase_admin import credentials, firestore  # AI used to explain this import 
from datetime import datetime  

# Load secret keys and paths from the .env file
# This way we don't hardcode any sensitive info
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "secrets", ".env")  # AI used to simplify this line and understand path handling
load_dotenv(dotenv_path)

# Get the path to the Firebase key file (this is like the "master key" to the database)
cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# Connect to Firestore
cred = credentials.Certificate(cred_path)
if not firebase_admin._apps:                # Avoid initializing multiple times
    firebase_admin.initialize_app(cred)

# This creates a Firestore client to interact with the database
# Use 'db' to read/write stuff from Firestore
db = firestore.client()

# ---------------- CRUD FUNCTIONS ---------------- #   (AI-generated label)
def add_habit(user_id, habit_name, target_per_week):
    """
    Add a new habit document to the 'habits' collection in Firestore.
    Each habit tracks user_id, habit name, target completions, completed times, and last updated timestamp.
    """

    # AI used to generate the structure of the document being added
    db.collection("habits").add({   
        "user_id": user_id,
        "habit_name": habit_name,
        "target_per_week": target_per_week,
        "completed_times": 0,    # New habit starts at 0 completions
        "last_updated": datetime.now().strftime("%b %d, %Y %I:%M %p") # Much simplier and easier format
    })

    print(f"\nHabit '{habit_name}' added!")

def print_habits(user_id):
    """
    Retrieves and display all habits for a specific user.
    Iterates over documents in the 'habits' collection filtered by user_id.
    """

    print("\nYour Habits:")
    habits = db.collection("habits").where("user_id", "==", user_id).stream()  # AI used to understand querying in Firestore
    found = False

    for doc in habits:
        found = True   
        data = doc.to_dict()   # Convert document to dictionary
        # AI used to format the output nicely
        print(f"""\nID: {doc.id}\nHabit: {data['habit_name']}\nTarget per week: {data['target_per_week']}\nCompleted: {data['completed_times']}\nLast updated: {data['last_updated']}""")
        print("----------------------------\n")

    if not found:    # Checks if any habits were found
        print("No habits found yet. Add one to get started!")

def update_habit(habit_id, updates):
    """
    Update a habit document by its document ID.
    The 'updates' parameter is a dictionary with field names and new values.
    """

    db.collection("habits").document(habit_id).update(updates)   # Update the document with new values
    print("\nHabit updated successfully.")


def delete_habit(habit_id):
    """
    Delete a habit document by its ID from the 'habits' collection.
    """

    db.collection("habits").document(habit_id).delete()   # Delete the document
    print("\nHabit deleted successfully.")

def log_completion(habit_id):
    """
    Add to the 'completed_times' field and update the 'last_updated' timestamp for a habit.
    Checks if the habit exists first.
    """

    doc_ref = db.collection("habits").document(habit_id)  
    doc = doc_ref.get()      # Retrieve the document to check existence

    if doc.exists:
        data = doc.to_dict()  # Convert document to dictionary
        new_count = data.get("completed_times", 0) + 1   # Increment completed_times by 1 and store in new_count
        doc_ref.update({
            "completed_times": new_count,  # Update completed_times
            "last_updated": datetime.now().strftime("%b %d, %Y %I:%M %p")  # Update timestamp
        })
        print(f"\nHabit progress updated! Total completions: {new_count}")
    else:  
        print("Habit not found.") 
