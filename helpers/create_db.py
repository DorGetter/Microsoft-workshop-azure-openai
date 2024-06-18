import sqlite3
import pandas as pd

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('../employees.db')
cursor = conn.cursor()

# Create the Employees table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Employees (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    email_address TEXT NOT NULL,
    role TEXT NOT NULL,
    rank TEXT NOT NULL,
    country TEXT NOT NULL
)
''')

# Insert sample data into Employees table
employees = [
    ('John', 'Doe', '555-1234', 'john.doe@example.com', 'Manager', 'senior', 'US'),
    ('Jane', 'Smith', '555-5678', 'jane.smith@example.com', 'Developer', 'mid', 'UK'),
    ('Alice', 'Johnson', '555-8765', 'alice.johnson@example.com', 'HR', 'junior', 'IL'),
    ('Bob', 'Brown', '555-4321', 'bob.brown@example.com', 'Manager', 'mid', 'US'),
    ('Carol', 'Davis', '555-6789', 'carol.davis@example.com', 'Developer', 'senior', 'UK'),
    ('Dave', 'Wilson', '555-9876', 'dave.wilson@example.com', 'HR', 'mid', 'IL'),
    ('Eve', 'Miller', '555-3456', 'eve.miller@example.com', 'Manager', 'junior', 'US'),
    ('Frank', 'Moore', '555-6543', 'frank.moore@example.com', 'Developer', 'mid', 'UK'),
    ('Grace', 'Taylor', '555-7890', 'grace.taylor@example.com', 'HR', 'senior', 'IL'),
    ('Hank', 'Anderson', '555-0123', 'hank.anderson@example.com', 'Manager', 'senior', 'US'),
    ('Ivy', 'Thomas', '555-3210', 'ivy.thomas@example.com', 'Developer', 'junior', 'UK'),
    ('Jack', 'Jackson', '555-7654', 'jack.jackson@example.com', 'HR', 'mid', 'IL'),
    ('Kathy', 'White', '555-4321', 'kathy.white@example.com', 'Manager', 'junior', 'US'),
    ('Liam', 'Harris', '555-6789', 'liam.harris@example.com', 'Developer', 'senior', 'UK'),
    ('Mia', 'Martin', '555-9876', 'mia.martin@example.com', 'HR', 'junior', 'IL'),
    ('Nina', 'Thompson', '555-3456', 'nina.thompson@example.com', 'Manager', 'mid', 'US'),
    ('Oscar', 'Garcia', '555-6543', 'oscar.garcia@example.com', 'Developer', 'junior', 'UK'),
    ('Paul', 'Martinez', '555-7890', 'paul.martinez@example.com', 'HR', 'senior', 'IL'),
    ('Quincy', 'Robinson', '555-0123', 'quincy.robinson@example.com', 'Manager', 'mid', 'US'),
    ('Rachel', 'Clark', '555-3210', 'rachel.clark@example.com', 'Developer', 'senior', 'UK'),
    ('Sam', 'Lewis', '555-7654', 'sam.lewis@example.com', 'HR', 'mid', 'IL'),
    ('Tina', 'Walker', '555-4321', 'tina.walker@example.com', 'Manager', 'junior', 'US'),
    ('Ursula', 'Hall', '555-6789', 'ursula.hall@example.com', 'Developer', 'mid', 'UK'),
    ('Vince', 'Allen', '555-9876', 'vince.allen@example.com', 'HR', 'senior', 'IL'),
    ('Wendy', 'Young', '555-3456', 'wendy.young@example.com', 'Manager', 'junior', 'US'),
    ('Xander', 'King', '555-6543', 'xander.king@example.com', 'Developer', 'senior', 'UK'),
    ('Yara', 'Scott', '555-7890', 'yara.scott@example.com', 'HR', 'mid', 'IL'),
    ('Zane', 'Green', '555-0123', 'zane.green@example.com', 'Manager', 'mid', 'US'),
    ('Amy', 'Adams', '555-3210', 'amy.adams@example.com', 'Developer', 'junior', 'UK'),
    ('Brian', 'Baker', '555-7654', 'brian.baker@example.com', 'HR', 'senior', 'IL')
]

# Insert data into the table
cursor.executemany('''
INSERT INTO Employees (first_name, last_name, phone_number, email_address, role, rank, country)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', employees)

# Commit changes
conn.commit()

# Fetch all rows from the Employees table
cursor.execute('SELECT * FROM Employees')
rows = cursor.fetchall()

# Convert to DataFrame for easier viewing
df = pd.DataFrame(rows, columns=['id', 'first_name', 'last_name', 'phone_number', 'email_address', 'role', 'rank', 'country'])



# Close the connection
conn.close()