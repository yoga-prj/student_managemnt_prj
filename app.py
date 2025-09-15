from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
import secrets
import os

app = Flask(__name__)

app.secret_key = '0bf336c3c7a9cb3a396f9253e42fab24'

# Database configuration
db = mysql.connector.connect(
    host=os.environ.get('DB_HOST', 'localhost'),
    user=os.environ.get('DB_USER', 'root'),
    password=os.environ.get('DB_PASSWORD', 'Yoga@mysql100#'),
    database=os.environ.get('DB_NAME', 'students_db')
)

cursor = db.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM students ORDER BY id ASC")
    students = cursor.fetchall()
    return render_template('dashboard.html', students=students)

# Add student
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        department = request.form['department']

        query = "INSERT INTO students (name, age, department) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, age, department))
        db.commit()

        flash('Student added successfully!')
        return redirect(url_for('index'))

    return render_template('add.html')

# Edit student
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    cursor.execute("SELECT * FROM students WHERE id = %s", (id,))
    student = cursor.fetchone()

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        department = request.form['department']

        query = "UPDATE students SET name=%s, age=%s, department=%s WHERE id=%s"
        cursor.execute(query, (name, age, department, id))
        db.commit()

        flash('Student updated successfully!')
        return redirect(url_for('index'))

    return render_template('edit.html', student=student)

# Delete student
@app.route('/delete/<int:id>', methods=['GET'])
def delete_student(id):
    cursor.execute("DELETE FROM students WHERE id = %s", (id,))
    db.commit()
    flash('Student deleted successfully!')
    return redirect(url_for('index'))

# Run the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(debug=True, host="0.0.0.0", port=port)
