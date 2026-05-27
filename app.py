from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# function to connect DB
def get_db():
    return sqlite3.connect('notes.db')


# HOME PAGE → show all notes
@app.route('/')
def home():
    conn = get_db()
    notes = conn.execute("SELECT * FROM notes").fetchall()
    conn.close()
    return render_template('home.html', notes=notes)


# ADD NOTE
@app.route('/add', methods=['POST'])
def add_note():
    title = request.form['title']
    content = request.form['content']

    conn = get_db()
    conn.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    conn.close()

    return redirect('/')


# DELETE NOTE
@app.route('/delete/<int:id>')
def delete_note(id):
    conn = get_db()
    conn.execute("DELETE FROM notes WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect('/')


if __name__ == '__main__':
    app.run()


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
