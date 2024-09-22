# Habit Tracker


## Project Description
The Habit Tracker is a simple yet powerful command-line application that allows users to create, track, and analyze habits. Users can manage daily or weekly habits, mark them as complete, and analyze their progress through streaks. The application is designed to help users develop good habits and maintain consistency.

## Installation and Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/habit-tracker.git
   cd habit-tracker

2. Set Up a Virtual Environment (Optional but recommended)
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies
    ```bash
    pip install -r requirements.txt  # If you have a requirements.txt file

4. Run the application
    ```bash
    python habit_tracker_app.py


## How to Use the Command-Line Interface
The Habit Tracker includes a command-line interface (CLI) for managing your habits. 
Here are the available commands:

- Create a Habit
  ```bash
  python cli.py --create "Habit Name" "daily"  # or "weekly"

- Mark a Habit as Complete
  ```bash
  python cli.py --complete "Habit Name"

- List All Habits
  ```bash
  python cli.py --list

- List Habits by Frequency
  ```bash
  python cli.py --periodicity "daily"  # or "weekly"

- Check Streak for a Habit
  ```bash
  python cli.py --streak "Habit Name"

- Get Habit with the Longest Streak
  ```bash
  python cli.py --longest-streak

- Delete a Habit
  ```bash
  python cli.py --delete "Habit Name"

## Examples of Usage

- Creating a Habit
  ```bash
  python cli.py --create "Exercise" "daily"

- Marking a Habit Complete
  ```bash
  python cli.py --complete "Exercise"

- Listing All Habits
  ```bash
  python cli.py --list

- Checking the Longest Streak
  ```bash
  python cli.py --longest-streak

## Requirements

- Python 3.x
- datetime and json modules (included in Python standard library)


### Instructions for Use

- Replace `yourusername` with your actual GitHub username in the clone command.
- Adjust any details as necessary to fit your project specifics. 

Feel free to copy and paste this content into a `README.md` file in your project directory!


