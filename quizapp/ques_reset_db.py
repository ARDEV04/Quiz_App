import sqlite3

def clean_questions_db():
    """Clean the questions database by dropping and recreating the table."""
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()

    # Drop and recreate the questions table
    cursor.execute("DROP TABLE IF EXISTS questions")
    cursor.execute("""
        CREATE TABLE questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            option1 TEXT NOT NULL,
            option2 TEXT NOT NULL,
            option3 TEXT NOT NULL,
            option4 TEXT NOT NULL,
            correct_option INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    print("Cleaned questions database (questions.db).")
    conn.close()

if __name__ == "__main__":
    clean_questions_db()
