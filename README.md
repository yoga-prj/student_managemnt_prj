# 🎓 Student Management System

A **Flask-based Student Management System** with **MySQL integration** to manage student records.  
The app provides full **CRUD functionality** (Add, Edit, Delete, View) with a responsive Bootstrap UI.

---

## 🚀 Features
- Add new student records with auto-generated IDs.
- Edit and update student details.
- Delete records with confirmation.
- Responsive table design with Bootstrap.
- MySQL database integration for reliable data storage.

---

## 🛠️ Tools & Technologies Used
- **Backend:** Python (Flask)  
- **Frontend:** HTML5, CSS3, Bootstrap  
- **Database:** MySQL  
- **Version Control:** Git & GitHub  
- **Deployment (Optional):** Render / Railway  

---

## 📂 Project Structure
student_prj/

│── app.py 

│── templates/ # HTML files (index, add, edit)

│── static/ # CSS, JS, assets

│── README.md 


---

## ⚡ Installation & Setup
1. Clone the repository  
   ```bash
   git clone https://github.com/your-username/student_prj.git
   cd student_prj
   
2. Create & activate virtual environment
    ```bash
   python -m venv .venv
   source .venv/bin/activate   # Mac/Linux
   .venv\Scripts\activate      # Windows

3. Install dependencies
    ```bash
    pip install flask mysql-connector-python

4. Create MySQL database
   ```bash
   CREATE DATABASE student_db;
   
5. Update app.py with DB credentials
   ```bash
   app.config['DB_HOST'] = "localhost"
   app.config['DB_USER'] = "your_username"
   app.config['DB_PASSWORD'] = "your_password"
   app.config['DB_NAME'] = "student_db"
   
6. Run the application
   ```bash
   python app.py
   
7. Open in browser
   ```bash
   cpp
   http://127.0.0.1:5000

📸 Screenshots
<img width="1440" height="900" alt="Screenshot 2025-09-15 at 10 23 01 PM" src="https://github.com/user-attachments/assets/c82ef78c-eb8a-40ca-8462-27852f891fd1" />
<img width="1440" height="900" alt="Screenshot 2025-09-15 at 10 23 48 PM" src="https://github.com/user-attachments/assets/6fc42223-14b7-4142-96e8-410c63f05b7e" />
<img width="1440" height="900" alt="Screenshot 2025-09-15 at 10 24 08 PM" src="https://github.com/user-attachments/assets/0f3453c8-c422-4de8-b3db-a16a392cf234" />


📜 License
```bash
This project is for learning purposes only.
