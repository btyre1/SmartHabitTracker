from dotenv import load_dotenv
import os
import firebase_admin
from firebase_admin import credentials, firestore

# Load the .env file from the secrets folder
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "secrets", ".env")
load_dotenv(dotenv_path=dotenv_path)

# Get the path to Firebase key
cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
if not cred_path:
    raise ValueError("GOOGLE_APPLICATION_CREDENTIALS not set in .env file")

# Initialize Firebase
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

db = firestore.client()

