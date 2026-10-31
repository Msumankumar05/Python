import sqlite3

con = None
try:
    
    con = sqlite3.connect("student_db.db")
    cur = con.cursor()
    
   
    cur.execute("SELECT * FROM Employee")
    rows = cur.fetchall()
    
    
    print("-" * 65)
    print(f"{'ID':<8}{'Name':<20}{'Salary':<15}{'Department':<15}")
    print("-" * 65)
    

    for row in rows:
        salary_val = row[2] if row[2] is not None else 0.0
        print(f"{row[0]:<8}{row[1]:<20}{salary_val:<15.2f}{row[3]:<15}")
        
    print("-" * 65)

except sqlite3.Error as e:
    print("❌ Database error:", e)

finally:
    if con is not None:
        con.close()
        print("🔌 Database connection closed.")
