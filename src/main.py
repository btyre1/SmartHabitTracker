from firestore_service import add_habit, print_habits

def main():
    print("Welcome to Smart Habit Tracker!")
    add_habit("test_user", "Exercise", 3)
    print_habits("test_user")

if __name__ == "__main__":
    main()