from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = '0bf336c3c7a9cb3a396f9253e42fab24'  # fixed secret key

# Database configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yoga@mysql100#",
    database="students_db"
)

cursor = db.cursor()

# Helper: Get students and auto-reset IDs
def get_students():
    cursor.execute("SELECT id, name, age, department FROM students ORDER BY id")
    students = cursor.fetchall()
    # Reset IDs to start from 1
    students_with_new_id = [(i+1, s[1], s[2], s[3]) for i, s in enumerate(students)]
    return students_with_new_id

# Home page
@app.route('/')
def index():
    students = get_students()
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
    cursor.execute("SELECT * FROM students ORDER BY id")
    students = cursor.fetchall()
    if id > len(students) or id < 1:
        flash('Invalid student ID!')
        return redirect(url_for('index'))
    student = students[id-1]

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        department = request.form['department']

        query = "UPDATE students SET name=%s, age=%s, department=%s WHERE id=%s"
        cursor.execute(query, (name, age, department, student[0]))
        db.commit()

        flash('Student updated successfully!')
        return redirect(url_for('index'))

    return render_template('edit.html', student=student)

# Delete student
@app.route('/delete/<int:id>', methods=['GET'])
def delete_student(id):
    students = get_students()
    if id > len(students) or id < 1:
        flash('Invalid student ID!')
        return redirect(url_for('index'))
    student_id = id  # actual DB ID

    # Find DB ID
    cursor.execute("SELECT id FROM students ORDER BY id")
    db_ids = cursor.fetchall()
    db_id_to_delete = db_ids[id-1][0]

    cursor.execute("DELETE FROM students WHERE id=%s", (db_id_to_delete,))
    db.commit()
    flash('Student deleted successfully!')
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, port=5001)
