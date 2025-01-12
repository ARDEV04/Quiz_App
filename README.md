# Quiz App Project

This project is a Python-based **Quiz Application** built using **Tkinter** for the GUI, and **SQLite** for database management. It allows users to take quizzes, view their scores, and stores both questions and results in separate databases.

---

## Features

- **User-Friendly Interface**: Built with Tkinter for an intuitive and interactive GUI.
- **Question Database**: Stores quiz questions with options and correct answers in `questions.db`.
- **Result Database**: Saves user scores and timestamps in `results.db`.
- **Animations**: Displays animations between questions for a better user experience.
- **Validation**: Ensures users select an option before proceeding to the next question.
- **Results Viewer**: A separate script to view all stored quiz results.
- **Reset Databases**: A script to clean and reset both the question and result databases.

---

## Installation
1. Install Python (if not already installed):
   - Download and install Python from [python.org](https://www.python.org/downloads/).

2. Install required libraries:
   No additional libraries are required; Tkinter and SQLite are included with Python.

---

## Usage

### 1. Setting Up Questions
1. Open the `setup_qeustion_db.py` database.
2. Add questions to the `questions` table in the following format:
   - `question` (TEXT): The question text.
   - `option1` (TEXT): First option.
   - `option2` (TEXT): Second option.
   - `option3` (TEXT): Third option.
   - `option4` (TEXT): Fourth option.
   - `correct_option` (INTEGER): The number (1-4) representing the correct answer.

You can use an SQLite editor or write scripts to populate the database.

### 2. Setting Up Results
1. Open the `setup_result_db.py` database.
2. A table is created where results will be stored.

### 3. Running the Quiz
Run the main application:
```bash
python quiz_app.py
```
Follow the instructions on the GUI to take the quiz.

### 3. Viewing Results
To view the results stored in `results.db`, run:
```bash
python view_results.py
```
This will display all user scores along with their timestamps.

### 4. Resetting Databases
To reset both the `questions` and `results` databases, run:
```bash
python ques_reset_db.py
python result_reset_db.py
```
This will drop and recreate the database tables, leaving them empty.

---

## File Structure

```
quiz-app/
├── quiz_app.py         # Main quiz application script
├── ques_reset_db.py    # Script to reset question database
├── result_reset_db.py  # Script to reset results database
├── view_results.py     # Script to view quiz results
├── questions.db        # SQLite database for quiz questions
├── results.db          # SQLite database for quiz results
├── README.md           # Project documentation
```

---

## Example Screenshots

### Home Screen
![Home Screen]([path/to/home_screen_screenshot.png](https://github.com/ARDEV04/Quiz_App/blob/main/quizapp/Screenshot%202025-01-12%20112024.png))

### Question Screen
![Question Screen](path/to/question_screen_screenshot.png)

### Results Viewer
![Results Viewer](path/to/results_viewer_screenshot.png)

---

## Future Enhancements
- **Dynamic Question Addition**: Add a feature to input questions directly through the app.
- **Leaderboard**: Display the top scores from all users.
- **Category Selection**: Allow users to select quiz categories.
- **Time-Limited Questions**: Add a timer for answering each question.

---

## Contributing
Contributions are welcome! Feel free to fork this repository, make your changes, and submit a pull request.

---

## Contact
For any questions or suggestions, please contact:
- **Name**: Anish Ranjan
- **Email**: [anish.ranjan004@gmail.com](mailto:anish.ranjan004@gmail.com)

---

