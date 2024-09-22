import datetime
from habit import Habit  # Adjust the import based on your project structure

def longest_streak_for_habit(habit):
    """
    Calculate the longest streak of consecutive completions based on the habit's periodicity.

    Args:
        habit (Habit): The Habit instance to analyze.

    Returns:
        int: The longest streak of consecutive completions.
    """
    if not habit.completed_dates:
        return 0

    # Sort the completed dates to ensure they're in chronological order
    habit.completed_dates.sort()

    # Initialize longest and current streak counters
    longest_streak = 1
    current_streak = 1

    # Set the required gap based on the habit's frequency
    if habit.frequency == 'daily':
        required_gap = 1  # Daily habits should have 1-day gaps
    elif habit.frequency == 'weekly':
        required_gap = 7  # Weekly habits should have 7-day gaps
    else:
        raise ValueError(f"Unknown frequency: {habit.frequency}")

    # Loop through the completed dates to calculate the streak
    for i in range(1, len(habit.completed_dates)):
        # Calculate the gap between two consecutive completions
        day_diff = (habit.completed_dates[i] - habit.completed_dates[i - 1]).days

        # If the gap matches the expected frequency (daily or weekly), increment the streak
        if day_diff == required_gap:
            current_streak += 1
        else:
            # Otherwise, reset the current streak
            current_streak = 1

        # Update the longest streak if the current one is longer
        longest_streak = max(longest_streak, current_streak)

    return longest_streak

def longest_streak_of_all_habits(habits):
    """
    Find the habit with the longest streak among all habits.

    Args:
        habits (list): List of Habit instances to analyze.

    Returns:
        tuple: A tuple containing the habit with the longest streak and its length.
    """
    if not habits:
        return None, 0

    streaks = {habit.name: longest_streak_for_habit(habit) for habit in habits}
    longest_habit_name = max(streaks, key=streaks.get)
    return longest_habit_name, streaks[longest_habit_name]
