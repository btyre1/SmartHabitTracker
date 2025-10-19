# Import functions from auth_service and firestore_service
from auth_service import sign_up, sign_in, sign_out
from firestore_service import add_habit, print_habits, update_habit, delete_habit, log_completion

# ---------------- MENU FUNCTIONS ---------------- # (AI-generated label)
def habit_menu(user_id):
    """
    Menu for all habit operations.
    Everything from adding to marking completion happens here.
    """

    while True:        # Display menu until user logs out (AI used for menu creation)
        print("\nSmart Habit Tracker")
        print("1. Add habit")
        print("2. View habits")
        print("3. Update habit")
        print("4. Delete habit")
        print("5. Mark habit as complete")
        print("6. Log out")

        choice = input("\nChoose an option: ").strip()   # Get user choice

        if choice == "1":       # Add habit
            name = input("Habit name: ").strip()   # Get habit name
            target = int(input("Target per week: "))   # Get target completions
            add_habit(user_id, name, target)  # Call add_habit function

        elif choice == "2":     # View habits
            print_habits(user_id)   # Call print_habits function

        elif choice == "3":     # Update habit
            doc_id = input("Enter habit ID to update: ").strip()   # Get document ID
            field = input("What field do you want to update (habit_name/target_per_week)? ").strip()   # Get field to update
            value = input("Enter new value: ").strip()   # Get new value
            if field == "target_per_week":  # Convert to int if updating target_per_week
                value = int(value)
            update_habit(doc_id, {field: value})  # Call update_habit function

        elif choice == "4":     # Delete habit
            doc_id = input("Enter habit ID to delete: ").strip()   # Get document ID
            delete_habit(doc_id)     # Call delete_habit function

        elif choice == "5":     # Mark habit as complete
            doc_id = input("Enter habit ID to mark complete: ").strip()   # Get document ID
            log_completion(doc_id)   # Call log_completion function

        elif choice == "6":     # Logout and return to auth menu
            sign_out()   # Call sign_out function
            break       # Exit habit menu
        else:          # Invalid choice
            print("Invalid choice, please try again.")


def auth_menu():
    """
    Menu for user authentication, includes sign up, sign in, or exit.
    """

    while True:         # Display menu until user exits (AI used for menu creation)
        print("\nWelcome to Smart Habit Tracker!")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")

        choice = input("Choose: ").strip()  # Get user choice

        if choice == "1":       # Sign up
            email = input("Email: ").strip()   # Get email
            password = input("Password: ").strip()   # Get password
            uid = sign_up(email, password)  # Call sign_up function
            if uid:   
                habit_menu(uid)   # If sign-up successful, go to habit menu
        elif choice == "2":     # Sign in
            email = input("Email: ").strip()  # Get email
            password = input("Password: ").strip()  # Get password
            uid = sign_in(email, password)  # Call sign_in function
            if uid:
                habit_menu(uid)  # If sign-in successful, go to habit menu
        elif choice == "3":     # Exit program
            print("\nGoodbye!")
            break
        else:      # Invalid choice
            print("Invalid option. Try again.")

# ---------------- START THE APP ---------------- # (AI-generated label)
if __name__ == "__main__":
    auth_menu()
