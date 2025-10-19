from auth_service import sign_up, sign_in, sign_out
from firestore_service import add_habit, print_habits, update_habit, delete_habit, log_completion

def habit_menu(user_id):

    while True:
        print("\nSmart Habit Tracker")
        print("1. Add habit")
        print("2. View habits")
        print("3. Update habit")
        print("4. Delete habit")
        print("5. Mark habit as complete")
        print("6. Log out")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            name = input("Habit name: ").strip()
            target = int(input("Target per week: "))
            add_habit(user_id, name, target)

        elif choice == "2":
            print_habits(user_id)

        elif choice == "3":
            doc_id = input("Enter habit ID to update: ").strip()
            field = input("What field do you want to update (habit_name/target_per_week)? ").strip()
            value = input("Enter new value: ").strip()
            if field == "target_per_week":
                value = int(value)
            update_habit(doc_id, {field: value})

        elif choice == "4":
            doc_id = input("Enter habit ID to delete: ").strip()
            delete_habit(doc_id)

        elif choice == "5":
            doc_id = input("Enter habit ID to mark complete: ").strip()
            log_completion(doc_id)

        elif choice == "6":
            sign_out()
            break
        else:
            print("Invalid choice, please try again.")

def auth_menu():

    while True:
        print("\nWelcome to Smart Habit Tracker!")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            email = input("Email: ").strip()
            password = input("Password: ").strip()
            uid = sign_up(email, password)
            if uid:
                habit_menu(uid)
        elif choice == "2":
            email = input("Email: ").strip()
            password = input("Password: ").strip()
            uid = sign_in(email, password)
            if uid:
                habit_menu(uid)
        elif choice == "3":
            print("\nGoodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    auth_menu()
