import json
from habit import Habit
from utils import save_habits_to_json, load_habits_from_json
from analytics import longest_streak_for_habit, longest_streak_of_all_habits

def main():
    """
    Main function to run the habit tracker application.
    """
    print("Welcome to the Habit Tracker!")
    habits = load_habits_from_json()  # Load existing habits

    while True:
        print("\nOptions:")
        print("1. Create Habit")
        print("2. Complete Habit")
        print("3. List All Habits")
        print("4. Check Streak for Habit")
        print("5. Get Habit with Longest Streak")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter habit name: ")
            frequency = input("Enter frequency (daily/weekly): ")
            habit = Habit(name, frequency)
            habits.append(habit)
            save_habits_to_json(habits)
            print(f"Habit '{name}' created.")

        elif choice == '2':
            name = input("Enter habit name to mark complete: ")
            for habit in habits:
                if habit.name == name:
                    habit.mark_complete()
                    save_habits_to_json(habits)
                    print(f"Habit '{habit.name}' marked as complete.")
                    break
            else:
                print("Habit not found.")

        elif choice == '3':
            print("All habits:")
            for habit in habits:
                print(f"{habit.name} ({habit.frequency})")

        elif choice == '4':
            name = input("Enter habit name to check streak: ")
            for habit in habits:
                if habit.name == name:
                    streak = longest_streak_for_habit(habit)
                    print(f"Longest streak for '{habit.name}': {streak}")
                    break
            else:
                print("Habit not found.")

        elif choice == '5':
            longest_habit_name, length = longest_streak_of_all_habits(habits)
            if longest_habit_name:
                print(f"Longest streak is for habit '{longest_habit_name}': {length}")
            else:
                print("No habits found.")

        elif choice == '6':
            print("Exiting the Habit Tracker. Goodbye!")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
