import sqlite3

def setup_questions_db():
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()
    
    # Create the questions table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            option1 TEXT NOT NULL,
            option2 TEXT NOT NULL,
            option3 TEXT NOT NULL,
            option4 TEXT NOT NULL,
            correct_option INTEGER NOT NULL
        )
    """)
    
    # Insert sample questions
    cursor.executemany("""
        INSERT INTO questions (question, option1, option2, option3, option4, correct_option)
        VALUES (?, ?, ?, ?, ?, ?)
    """, [
        ("What is 2 + 2?", "3", "4", "5", "6", 2),
        ("What is the capital of France?", "London", "Paris", "Berlin", "Madrid", 2),
        ("which is capital of Bihar","bhagalpur","Bihar","patna","champaran",3),
    ])
    
    conn.commit()
    print("Questions database setup completed.")
    conn.close()

if __name__ == "__main__":
    setup_questions_db()
