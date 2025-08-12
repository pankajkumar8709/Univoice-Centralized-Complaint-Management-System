import sqlite3

# Create or connect to a new SQLite database
conn = sqlite3.connect('newmycollege.db')
cursor = conn.cursor()

# Create students table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        roll_number TEXT PRIMARY KEY,
        password TEXT NOT NULL,
        name TEXT NOT NULL,
        course TEXT NOT NULL,
        sem TEXT NOT NULL,
        section TEXT NOT NULL
    )
''')

# Create teachers table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS teachers (
        employee_id TEXT PRIMARY KEY,
        password TEXT NOT NULL,
        name TEXT NOT NULL,
        department TEXT NOT NULL 
    )
''')

# Create admins table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS admins (
        admin_id TEXT PRIMARY KEY,
        password TEXT NOT NULL,
        name TEXT NOT NULL,
        category TEXT NOT NULL
    )
''')

# Sample student data
students = [
    ('24CSE394', '24CSE394', 'Pankaj Kumar Mahto', 'BTech CSE', '3rd', 'F'),
    ('24CSE428', '24CSE428', 'Kanak Shahgal', 'BTech CSE', '3rd', 'E')
]

# Sample teacher data
teachers = [
    ('EC001', 'EC001', 'Arpan Singh', 'CSE'),
    ('EC002', 'EC002', 'GVS Narayan', 'CSE')
]

# Sample admin data
admins = [
    ('AC001', 'AC001', 'Saroj', 'Hostel'),
    ('AC002', 'AC002', 'Suraj', 'Sports'),
    ('AC003', 'AC003', 'Ram', 'Bus'),
    ('AC004', 'AC004', 'Shubankar', 'Mess'),
    ('AC005', 'AC005', 'AVS Pawan Kalyan', 'Academics'),
    ('AC006', 'AC006', 'NVJ Rao', 'Officials'),
    ('AC007', 'AC007', 'Basic Amenities', 'Basic Amenities')
   
]

# Insert sample data (ignores if already exists)
cursor.executemany('INSERT OR IGNORE INTO students VALUES (?, ?, ?, ?, ?, ?)', students)
cursor.executemany('INSERT OR IGNORE INTO teachers VALUES (?, ?, ?, ?)', teachers)


cursor.executemany('INSERT OR IGNORE INTO admins VALUES (?, ?, ?, ?)',admins)



# Save and close
conn.commit()





# #
# new_admins = [
    
# ]

# cursor.executemany('INSERT OR IGNORE INTO admins VALUES (?, ?, ?, ?)',new_admins)



# # Save and close
# conn.commit()
conn.close()

print("✅ mycollege.db created successfully with sample data.")
