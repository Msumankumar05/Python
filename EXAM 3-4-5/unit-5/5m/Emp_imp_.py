import sqlite3

con = None
try:
    # 1. Establish database connection and cursor
    con = sqlite3.connect("Emp.db")
    cur = con.cursor()
    
    # 2. Create the Employee table structure
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Employee (
        emp_id INTEGER PRIMARY KEY,
        emp_name VARCHAR(50),
        salary FLOAT,
        dept VARCHAR(30)
    )
    """)
    
    # 3. Dynamic Loop to take inputs for 5 employees
    for i in range(5):
        print(f"\n--- Enter details of employee {i + 1} ---")
        emp_id = int(input("Employee ID: "))
        emp_name = input("Employee name: ")
        salary = float(input("Salary: "))
        dept = input("Department: ")
        
        # 4. Secure parameterized insertion query
        cur.execute(
            """INSERT INTO Employee (emp_id, emp_name, salary, dept)
               VALUES (?, ?, ?, ?)""",
            (emp_id, emp_name, salary, dept)
        )
        
    # 5. Commit all changes after the loop runs successfully
    con.commit()
    print("\n✅ Five employee records inserted successfully.")

except (sqlite3.Error, ValueError) as e:
    # 6. Safety check: Rollback if anything breaks mid-way
    if con is not None:
        con.rollback()
        print("\n🔄 Transaction rolled back due to error.")
    print("❌ Error:", e)

finally:
    # 7. Safe close statement wrapped securely
    if con is not None:
        con.close()
        print("🔌 Database connection closed.")
