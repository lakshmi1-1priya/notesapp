import sqlite3

conn = sqlite3.connect('notes.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT
)
""")

conn.commit()
conn.close()

print("DB created!")
