import os
from dotenv import load_dotenv
import pyrebase

# load .env (path relative to src/)
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "secrets", ".env")
load_dotenv(dotenv_path=dotenv_path)

config = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": os.getenv("FIREBASE_APP_ID"),
    "measurementId": os.getenv("FIREBASE_MEASUREMENT_ID")
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

# Store the current logged-in user
current_user = {"uid": None}

def sign_up(email, password):
    """Create a new user with email and password."""

    try:
        user = auth.create_user_with_email_and_password(email, password)
        current_user["uid"] = user["localId"]
        print("\nSign-up successful.")
        return user["localId"]
    except Exception as e:
        print("\nSign-up failed:", e)
        return None

def sign_in(email, password):
    """Log in an existing user."""

    try:
        user = auth.sign_in_with_email_and_password(email, password)
        current_user["uid"] = user["localId"]
        print("\nLogged in successfully.")
        return user["localId"]
    except Exception as e:
        print("\nLogin failed:", e)
        return None

def sign_out():
    """Sign out the current user."""
    
    current_user["uid"] = None
    print("\n👋 Signed out.")


