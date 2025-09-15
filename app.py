import os
import mysql.connector
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

db = mysql.connector.connect(
    host=os.environ.get("DB_HOST"),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASSWORD"),
    database=os.environ.get("DB_NAME")
)
cursor = db.cursor()

# Dashboard route
@app.route('/')
def dashboard():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return render_template('dashboard.html', students=students)

# Add student route
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        department = request.form['department']

        cursor.execute("INSERT INTO students (name, age, department) VALUES (%s, %s, %s)", 
                       (name, age, department))
        db.commit()
        return redirect('/')
    return render_template('add.html')

# Edit student route
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        department = request.form['department']

        cursor.execute("UPDATE students SET name=%s, age=%s, department=%s WHERE id=%s", 
                       (name, age, department, id))
        db.commit()
        return redirect('/')
    
    cursor.execute("SELECT * FROM students WHERE id=%s", (id,))
    student = cursor.fetchone()
    return render_template('edit.html', student=student)

# Delete student route
@app.route('/delete/<int:id>')
def delete_student(id):
    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    db.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
