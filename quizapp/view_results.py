import sqlite3

def view_results():
    # Connect to the quiz database
    conn = sqlite3.connect('results.db')
    cursor = conn.cursor()
    # Query the scores table
    cursor.execute("SELECT username, score, date FROM scores ORDER BY date DESC")
    results = cursor.fetchall()
    # Print the results
    print("Quiz Results:")
    print(f"{'Name':<20} {'Score':<10} {'Date':<20}")
    print("-" * 50)
    for result in results:
        print(f"{result[0]:<20} {result[1]:<10} {result[2]:<20}")
    # Close the database connection
    conn.close()
if __name__ == "__main__":
    view_results()
