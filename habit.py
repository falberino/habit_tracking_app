import datetime

class Habit:
    """
    A class to represent a habit.

    Attributes:
        name (str): Name of the habit.
        frequency (str): Frequency of the habit ('daily' or 'weekly').
        created_at (datetime): Timestamp of habit creation.
        completed_dates (list): List of timestamps when the habit was completed.
    """
    def __init__(self, name, frequency, created_at=None, completed_dates=None):
        """
        Initialize a Habit instance.

        Args:
            name (str): Name of the habit.
            frequency (str): Frequency of the habit ('daily' or 'weekly').
            created_at (datetime, optional): Timestamp of habit creation. Defaults to current time.
            completed_dates (list, optional): List of timestamps when the habit was completed.
        """
        # Set habit name and frequency (daily or weekly)
        self.name = name
        self.frequency = frequency

        # Set creation timestamp, defaulting to now if not provided
        self.created_at = created_at if created_at else datetime.datetime.now()

        # Initialize completed dates list (empty by default)
        self.completed_dates = completed_dates if completed_dates else []

    def mark_complete(self):
        """
        Mark the habit as complete by appending the current timestamp to completed_dates.
        """
        # Add current timestamp to completed_dates when habit is completed
        self.completed_dates.append(datetime.datetime.now())
        
    def get_streak(self):
        """
        Get the current streak count.

        Returns:
            int: Number of times the habit has been completed.
        """
        # Return the number of times the habit has been marked as completed
        return len(self.completed_dates)
    
    def to_dict(self):
        """
        Convert the Habit instance to a dictionary suitable for JSON.

        Returns:
            dict: A dictionary representation of the Habit instance.
        """
        # Convert Habit object to a dictionary for easy JSON storage
        return {
            'name': self.name,
            'frequency': self.frequency,
            'created_at': self.created_at.isoformat(),
            'completed_dates': [date.isoformat() for date in self.completed_dates]
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create a Habit instance from a dictionary.

        Args:
            data (dict): Dictionary containing habit data.

        Returns:
            Habit: An instance of Habit initialized with the provided data.
        """
        # Convert a dictionary back into a Habit object
        return cls(
            name=data['name'],
            frequency=data['frequency'],
            created_at=datetime.datetime.fromisoformat(data['created_at']),
            completed_dates=[datetime.datetime.fromisoformat(date) for date in data['completed_dates']]
        )
