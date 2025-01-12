import sqlite3

def clean_results_db():
    """Clean the results database by dropping and recreating the table."""
    conn = sqlite3.connect('results.db')
    cursor = conn.cursor()

    # Drop and recreate the scores table
    cursor.execute("DROP TABLE IF EXISTS scores")
    cursor.execute("""
        CREATE TABLE scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            score INTEGER NOT NULL,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()
    print("Cleaned results database (results.db).")
if __name__ == "__main__":
    clean_results_db()