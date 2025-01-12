import sqlite3

def setup_results_db():
    conn = sqlite3.connect('results.db')
    cursor = conn.cursor()
    
    # Create the scores table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            score INTEGER NOT NULL,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conn.commit()
    print("Results database setup completed.")
    conn.close()

if __name__ == "__main__":
    setup_results_db()
