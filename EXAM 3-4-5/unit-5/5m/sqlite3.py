import sqlite3

try:
    # 1. Establish a connection to the database file
    # (If 'school.db' does not exist, SQLite will automatically create it)
    connection = sqlite3.connect("school.db")
    
    # 2. Create a cursor object to execute SQL commands
    cursor = connection.cursor()
    
    # 3. Write and execute the SQL query to create the Student table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Student (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT UNIQUE,
        enrollment_date TEXT DEFAULT CURRENT_TIMESTAMP
    );
    """
    cursor.execute(create_table_query)
    print("📋 'Student' table created successfully (or already exists).")
    
    # 4. Commit the changes to the database permanently
    connection.commit()
    print("💾 Changes committed successfully.")

except sqlite3.Error as error:
    print(f"❌ An error occurred while working with SQLite: {error}")

finally:
    # 5. Ensure the database connection is closed safely
    if connection:
        connection.close()
        print("🔌 Database connection closed.")
