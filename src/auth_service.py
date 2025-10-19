# AI helped with debugging this file
import os
from dotenv import load_dotenv  # AI used to explain this import 
import pyrebase

# Load secret keys and paths from the .env file
# This way we don't hardcode any sensitive info
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "secrets", ".env")  # AI used to simplify this line and understand path handling
load_dotenv(dotenv_path=dotenv_path) 

# Firebase configuration dictionary (AI used to generate this config structure)
config = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": os.getenv("FIREBASE_APP_ID"),
    "measurementId": os.getenv("FIREBASE_MEASUREMENT_ID"),
    "databaseURL": ""   # For debugging purposes, not used in this app 
}

# Initialize Pyrebase  (AI used to better understand pyrebase)
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

# Keep track of who is logged in right now
current_user = {"uid": None}

# ---------------- AUTH FUNCTIONS ---------------- #   (AI-generated label)
def sign_up(email, password):
    """
    Create a new user in Firebase Auth.
    Returns UID if successful, None if failed.
    """

    try:
        user = auth.create_user_with_email_and_password(email, password)       # Create user
        current_user["uid"] = user["localId"]       # Store UID of the logged-in user
        print("\nSign-up successful.")
        return user["localId"]
    except Exception as e:      # Catch any errors (like email already in use)
        print("\nSign-up failed:", e)
        return None

def sign_in(email, password):
    """
    Log in an existing user. 
    Returns UID if successful, None if failed.
    """

    try:
        user = auth.sign_in_with_email_and_password(email, password)     # Log in user
        current_user["uid"] = user["localId"]
        print("\nLogged in successfully.")
        return user["localId"]
    except Exception as e:   # Catch any errors (like wrong password)
        print("\nLogin failed:", e)
        return None

def sign_out():
    """Sign out the current user."""

    current_user["uid"] = None      # Clear the stored UID
    print("\n👋 Signed out.")


