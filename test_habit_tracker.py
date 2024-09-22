import unittest
from habit import Habit
from utils import save_habits_to_json, load_habits_from_json
from analytics import longest_streak_for_habit

class TestHabitTracker(unittest.TestCase):

    def setUp(self):
        """Set up a habit for testing."""
        self.habit = Habit("Test Habit", "daily")
        self.habit.completed_dates = [
            # Add predefined completed dates for testing
        ]

    def test_habit_creation(self):
        """Test habit creation."""
        self.assertEqual(self.habit.name, "Test Habit")
        self.assertEqual(self.habit.frequency, "daily")

    def test_mark_complete(self):
        """Test marking a habit as complete."""
        self.habit.mark_complete()
        self.assertEqual(len(self.habit.completed_dates), 1)

    def test_longest_streak(self):
        """Test the longest streak calculation."""
        self.habit.completed_dates = [
            # Populate with dates that create a streak
        ]
        streak = longest_streak_for_habit(self.habit)
        self.assertEqual(streak, expected_value)  # Replace expected_value with your expected result

    def test_load_habits(self):
        """Test loading habits from JSON."""
        save_habits_to_json([self.habit])
        loaded_habits = load_habits_from_json()
        self.assertEqual(len(loaded_habits), 1)
        self.assertEqual(loaded_habits[0].name, "Test Habit")

if __name__ == '__main__':
    unittest.main()
