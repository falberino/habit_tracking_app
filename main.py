from habit import Habit  # Import the Habit class
import json
from datetime import datetime, timedelta

def create_predefined_habits():
    """
    Create predefined habits with completion data over 4 weeks for testing purposes.
    
    Returns:
        list: A list of Habit instances with predefined completed_dates, covering daily 
              and weekly frequencies.
    """
    # Create habits
    habit1 = Habit("Exercise", "daily")
    habit2 = Habit("Read", "daily")
    habit3 = Habit("Meditate", "daily")
    habit4 = Habit("Go to church", "weekly")
    habit5 = Habit("Pilates", "weekly")

    # Define the completion pattern for the last 4 weeks
    today = datetime.now()

    # For Exercise: completed every day for 4 weeks
    habit1.completed_dates = [today - timedelta(days=i) for i in range(28)]  # Last 28 days

    # For Read: completed every 3 days for 4 weeks
    habit2.completed_dates = [today - timedelta(days=i) for i in range(0, 28, 3)]  # Days 0, 3, 6, ..., 27

    # For Meditate: completed every 4 days for 4 weeks
    habit3.completed_dates = [today - timedelta(days=i) for i in range(0, 28, 4)]  # Days 0, 4, 8, ..., 28

    # For Go to church: completed once a week for the last 4 weeks
    habit4.completed_dates = [today - timedelta(weeks=i) for i in range(4)]  # Weeks 0, 1, 2, 3

    # For Pilates: completed once a week for the last 4 weeks
    habit5.completed_dates = [today - timedelta(weeks=i) for i in range(4)]  # Weeks 0, 1, 2, 3

    return [habit1, habit2, habit3, habit4, habit5]

def save_habits_to_json(habits, file_name='habits.json'):
    """
    Save a list of habits to a JSON file.

    Args:
        habits (list): A list of Habit instances to save.
        file_name (str, optional): The name of the file to save habits to. Defaults to 'habits.json'.
    """
    with open(file_name, 'w') as f:
        json.dump([habit.to_dict() for habit in habits], f, indent=4)

if __name__ == "__main__":
    habits = create_predefined_habits()  # Create predefined habits
    save_habits_to_json(habits)          # Save them to JSON
    print("Predefined habits created and saved to habits.json.")
