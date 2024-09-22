import argparse
from habit import Habit
from utils import save_habits_to_json, load_habits_from_json
from analytics import longest_streak_for_habit, longest_streak_of_all_habits

# CLI setup

def list_all_habits(habits):
    """
    List all habit names.

    Args:
        habits (list): List of Habit instances.

    Returns:
        list: List of habit names.
    """
    # Return a list of habit names from the list of Habit objects
    return [habit.name for habit in habits]

def list_habits_by_periodicity(habits, frequency):
    """
    List habits by periodicity (frequency).

    Args:
        habits (list): List of Habit instances.
        frequency (str): 'daily' or 'weekly' frequency to filter habits.

    Returns:
        list: List of Habit instances with the given frequency.
    """
    # Filter habits by frequency (either 'daily' or 'weekly')
    return [habit for habit in habits if habit.frequency == frequency]

def cli():
    """
    Command Line Interface for managing and analyzing habits.

    Commands:
        --create name frequency: Create a new habit with the given name and frequency.
        --complete name: Mark a habit with the given name as complete.
        --list: List all habits.
        --periodicity frequency: List habits with the specified frequency ('daily' or 'weekly').
        --streak name: Get the longest streak for the habit with the given name.
        --longest-streak: Get the habit with the longest streak.
        --delete name: Delete a habit with the given name.
    """
    parser = argparse.ArgumentParser(description="Habit Tracker CLI")

    # Define arguments for different CLI operations
    parser.add_argument('--create', nargs=2, metavar=('name', 'frequency'), help="Create a new habit")
    parser.add_argument('--complete', metavar='name', help="Mark a habit as complete")
    parser.add_argument('--list', action='store_true', help="List all habits")
    parser.add_argument('--periodicity', metavar='frequency', help="List habits by frequency")
    parser.add_argument('--streak', metavar='name', help="Get the longest streak for a habit")
    parser.add_argument('--longest-streak', action='store_true', help="Get the habit with the longest streak")
    parser.add_argument('--delete', metavar='name', help="Delete a habit")

    args = parser.parse_args()

    # Load habits from JSON file
    habits = load_habits_from_json()

    if args.create:
        name, frequency = args.create
        habit = Habit(name, frequency)
        habits.append(habit)
        save_habits_to_json(habits)
        print(f"Habit '{name}' created.")

    elif args.complete:
        for habit in habits:
            if habit.name == args.complete:
                habit.mark_complete()
                save_habits_to_json(habits)
                print(f"Habit '{habit.name}' marked as complete.")
                break

    elif args.list:
        print("All habits:")
        for habit_name in list_all_habits(habits):
            print(habit_name)

    elif args.periodicity:
        filtered_habits = list_habits_by_periodicity(habits, args.periodicity)
        print(f"Habits with frequency '{args.periodicity}':")
        for habit in filtered_habits:
            print(habit.name)

    elif args.streak:
        for habit in habits:
            if habit.name == args.streak:
                print(f"Longest streak for habit '{habit.name}': {longest_streak_for_habit(habit)}")
                break

    elif args.longest_streak:
        longest_habit_name, length = longest_streak_of_all_habits(habits)
        if longest_habit_name:
            print(f"Longest streak is for habit '{longest_habit_name}': {length}")
