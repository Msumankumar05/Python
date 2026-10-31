import sqlite3

con = None
try:
    
    con = sqlite3.connect("student_db.db")
    cur = con.cursor()
    

    cur.execute("""
    UPDATE Employee
    SET salary = salary * 1.10
    WHERE dept = ?""", 
    ("IT",))
    
    
    
    print(f"📊 Rows affected: {cur.rowcount}")

    con.commit()
    print("✅ IT salaries updated successfully by 10%.")

except sqlite3.Error as e:
    
    if con is not None:
        con.rollback()
        print("🔄 Transaction rolled back due to an error.")
    print("❌ Database error:", e)

finally:
   
    if con is not None:
        con.close()
        print("🔌 Database connection closed.")
