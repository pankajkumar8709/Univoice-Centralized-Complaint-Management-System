import sqlite3

# Connect to SQLite DB (will create if it doesn't exist)
conn = sqlite3.connect('college.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        roll_number TEXT PRIMARY KEY,
        password TEXT NOT NULL,
        name TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS teachers (
        employee_id TEXT PRIMARY KEY,
        password TEXT NOT NULL,
        name TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS admins (
        admin_id TEXT PRIMARY KEY,
        password TEXT NOT NULL,
        name TEXT NOT NULL
    )
''')

# Insert sample student data
students = [
    ('101', 'pass123', 'Ravi Kumar'),
    ('102', 'pass234', 'Sneha Das'),
    ('103', 'pass345', 'Aman Verma')
]

# Insert sample teacher data
teachers = [
    ('T001', 'teach123', 'Pooja Mishra'),
    ('T002', 'teach234', 'Manish Rao')
]

# Insert sample admin data
admins = [
    ('admin1', 'admin123', 'Admin Master'),
    ('admin2', 'admin456', 'Super Admin')
]

cursor.executemany('INSERT OR IGNORE INTO students VALUES (?, ?, ?)', students)
cursor.executemany('INSERT OR IGNORE INTO teachers VALUES (?, ?, ?)', teachers)
cursor.executemany('INSERT OR IGNORE INTO admins VALUES (?, ?, ?)', admins)

# Commit and close
conn.commit()
conn.close()

print("✅ college.db created successfully with sample data.")
