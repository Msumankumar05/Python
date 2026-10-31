import sqlite3

con = None
try:
   
    con = sqlite3.connect("student_db.db")
    cur = con.cursor()
    
    cur.execute("""
    SELECT name 
    FROM sqlite_master 
    WHERE type = 'table'
    ORDER BY name
    """)
    
    print("📋 Available tables:")
    tables = cur.fetchall()
    
    if not tables:
        print(" (No tables found in this database)")
    else:
        for row in tables:
            print(f" - {row[0]}")
            
    print("-" * 40)
    
    cur.execute("ALTER TABLE emp ADD COLUMN salary INTEGER")
    
    con.commit()
    print("✅ Salary column added successfully to the 'emp' table.")

except sqlite3.Error as e:
    if con is not None:
        con.rollback()
        print("🔄 Structure modification rolled back.")
    print("❌ Database error:", e)

finally:
    if con is not None:
        con.close()
        print("🔌 Database connection closed.")
