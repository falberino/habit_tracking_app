import json
from habit import Habit

def save_habits_to_json(habits, file_name='habits.json'):
    """
    Save a list of habits to a JSON file.

    Args:
        habits (list): List of Habit instances to save.
        file_name (str, optional): Name of the file to save to. Defaults to 'habits.json'.
    """
    # Open file in write mode and dump the habits list as JSON
    with open(file_name, 'w') as f:
        json.dump([habit.to_dict() for habit in habits], f, indent=4)

def load_habits_from_json(file_name='habits.json'):
    """
    Load habits from a JSON file.

    Args:
        file_name (str, optional): Name of the file to load from. Defaults to 'habits.json'.

    Returns:
        list: List of Habit instances loaded from the JSON file.
    """
    try:
        # Open the JSON file and load it into a list of habit dictionaries
        with open(file_name, 'r') as f:
            habit_dicts = json.load(f)

        # Convert each dictionary back into a Habit object
        return [Habit.from_dict(h) for h in habit_dicts]
    except FileNotFoundError:
        # Return an empty list if the file doesn't exist
        return []
