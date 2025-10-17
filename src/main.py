from firestore_service import add_habit, print_habits, update_habit, delete_habit

def main():
    user_id = input("Enter your user ID: ")

    while True:
        print("\nSmart Habit Tracker")
        print("1. Add habit")
        print("2. View habits")
        print("3. Update habit")
        print("4. Delete habit")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Habit name: ")
            target = int(input("Target per week: "))
            add_habit(user_id, name, target)

        elif choice == "2":
            print_habits(user_id)

        elif choice == "3":
            doc_id = input("Enter habit ID to update: ")
            field = input("What field do you want to update (habit_name/target_per_week)? ")
            value = input("Enter new value: ")
            if field == "target_per_week":
                value = int(value)
            update_habit(doc_id, {field: value})

        elif choice == "4":
            doc_id = input("Enter habit ID to delete: ")
            delete_habit(doc_id)

        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
