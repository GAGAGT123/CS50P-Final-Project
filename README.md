# Task Manager 📋

#### Video Demo: <https://youtu.be/uM4iyCeK-yM?si=ttpeesf3zxXeehdN>

#### Description:
The **Task Manager** is a command-line application built in Python as my final project for **CS50's Introduction to Programming with Python**. It helps users organize and track their daily tasks efficiently. This application allows users to create, view, complete, and delete tasks, with persistent storage using JSON files.

## Project Structure

```

project/
├── project.py          # Main application with all core functions
├── test_project.py     # Unit tests for the application using pytest
├── tasks.json          # Data storage file (created automatically)
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies (pytest only)

```

## Functions in project.py

### Core Functions
- `main()`: The main program loop that displays the interactive menu and handles user input. It offers 7 options: add task, view all tasks, view pending tasks, view completed tasks, complete task, delete task, and exit.

- `add_task()`: Prompts the user for task details including title (required), description (optional), and priority level (high/medium/low, with medium as default). Returns a dictionary with all task data, initial status "pending", and an ISO-format timestamp.

- `view_tasks()`: Takes a list of tasks and a status filter ("all", "pending", or "completed"). Displays tasks in a formatted table with their ID, title, description, priority with emoji icons, and timestamps. Handles empty task lists gracefully.

- `complete_task()`: Accepts a task ID and marks the corresponding task as completed. Updates the task's status and adds a completion timestamp. Returns True if successful, False if the task ID doesn't exist or the task is already completed.

- `delete_task()`: Removes a task from the list based on its ID. Returns True if the task was found and deleted, False otherwise.

- `save_tasks()`: Writes the current tasks list to a JSON file using Python's json module with proper formatting (indent=2) for human readability. Assigns IDs sequentially before saving.

- `load_tasks()`: Reads tasks from the JSON file if it exists. Handles file not found errors by returning an empty list. Ensures each task has a unique ID by assigning them sequentially when loading.

### Helper Functions
- `get_priority_icon()`: Returns an emoji icon (🔴 for high, 🟡 for medium, 🟢 for low) based on the priority level for visual distinction.

- `format_date()`: Converts ISO-format datetime strings to a more readable format (YYYY-MM-DD HH:MM). Includes error handling for invalid date strings.

## test_project.py

The test file contains comprehensive unit tests using pytest with 7 test functions:
- `test_add_task()`: Tests task creation with mocked user input to verify all attributes are set correctly.
- `test_complete_task()`: Tests marking tasks as completed and ensures already completed tasks cannot be completed again.
- `test_delete_task()`: Tests task deletion with both valid and invalid IDs.
- `test_save_and_load_tasks()`: Tests data persistence to verify save/load functionality.
- `test_complete_task_already_completed()`: Tests edge case where user attempts to complete an already completed task.
- `test_add_task_default_priority()`: Tests that priority defaults to medium when no valid priority is provided.
- `test_add_task_empty_title()`: Tests that empty titles are rejected and user is prompted again.

## Design Choices

### Storage Format
I chose JSON for data storage because it's lightweight, human-readable, and doesn't require external dependencies. While SQLite would provide more powerful querying, JSON was sufficient for this project's scope and simpler to implement. JSON also makes it easy to debug and manually edit tasks if needed.

### Task IDs
Tasks use string IDs that are automatically assigned when saving to ensure consistency. This approach makes it easier to implement features like task references in the future.

### Priority System
Priority levels (high, medium, low) help users organize their tasks effectively. I added visual icons (🔴🟡🟢) to make priorities immediately recognizable. The default priority is set to medium to reduce user input friction.

### Error Handling
The application includes comprehensive error handling for invalid user input, missing files, and corrupted JSON data. The `load_tasks()` function gracefully handles missing JSON files by returning an empty list, preventing crashes on first run. Input validation ensures task titles cannot be empty.

## How to Run

1. Ensure Python 3.6 or higher is installed on your system.
2. Navigate to the project directory in your terminal:
   ```bash
   cd ~/project
```

1. Run the application:
   ```bash
   python project.py
   ```
2. Follow the interactive menu prompts to manage your tasks.

Testing

To run the unit tests:

```bash
pytest test_project.py -v
```

All tests should pass successfully. The -v flag provides verbose output showing each test's result.

Requirements

· Python 3.6+
· pytest (for running tests)

No external libraries are required for the main application, making it portable and easy to install on any system.

Future Improvements

· Add due dates for tasks with reminder notifications.
· Implement task categories or tags for better organization.
· Add search functionality to find specific tasks by title or description.
· Create a GUI version using tkinter for better user experience.
· Add data export options (CSV, PDF) for reporting.
· Implement recurring tasks that automatically regenerate.

What I Learned

This project reinforced several key concepts from CS50P:

· File I/O: Reading and writing JSON files for data persistence.
· Exception Handling: Gracefully handling file not found and JSON decode errors.
· Function Design: Creating modular functions with single responsibilities.
· Testing: Writing unit tests with pytest to ensure code reliability.
· User Input Validation: Handling edge cases and invalid user inputs.
· Datetime Manipulation: Formatting and storing timestamps in ISO format.
· Code Organization: Structuring a project with separate files for code and tests.

Conclusion

The Task Manager project successfully demonstrates a complete Python application with core functionality, robust error handling, and comprehensive testing. It serves as a practical tool for daily task management while showcasing the programming skills I developed throughout CS50's Introduction to Programming with Python. This project represents my understanding of Python fundamentals and my ability to create a well-structured, maintainable application.

