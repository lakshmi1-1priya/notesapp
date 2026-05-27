from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# 🔹 Database connection
def get_db():
    return sqlite3.connect('notes.db')


# 🔹 Initialize DB (VERY IMPORTANT for deployment)
def init_db():
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


# 🏠 Home route
@app.route('/')
def home():
    conn = get_db()
    notes = conn.execute("SELECT * FROM notes").fetchall()
    conn.close()
    return render_template('home.html', notes=notes)


# ➕ Add note
@app.route('/add', methods=['POST'])
def add_note():
    title = request.form['title']
    content = request.form['content']

    conn = get_db()
    conn.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    conn.close()

    return redirect('/')


# ❌ Delete note
@app.route('/delete/<int:id>')
def delete_note(id):
    conn = get_db()
    conn.execute("DELETE FROM notes WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect('/')


# 🚀 Run app
if __name__ == '__main__':
    init_db()  # ensures table exists
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
