# 🚀 Smart Expense Tracker API

A production-style backend built using **Django REST Framework** with **JWT Authentication** to securely manage user expenses.

This project demonstrates real-world backend engineering practices including custom authentication, protected APIs, relational database design, and scalable architecture.

---

## ⭐ Features

✅ Custom Email-Based User Authentication  
✅ JWT Login & Secure Token Authorization  
✅ Protected Expense APIs (User-specific data)  
✅ RESTful Architecture  
✅ Scalable App Structure  
✅ Admin Panel for Database Control  
✅ Production-Oriented Design  

---

## 🛠 Tech Stack

- **Python**
- **Django**
- **Django REST Framework**
- **JWT (SimpleJWT)**
- **SQLite** (Development)


## 📁 Project Structure
smart_expense_tracker/
│
├── users/        # Custom user authentication
├── expenses/     # Expense management APIs
├── config/       # Project settings

Built with modular architecture to support future scaling.

---

## 🔐 Authentication Flow

1. Register a new user  
2. Login to receive JWT tokens  
3. Send access token in headers  
4. Access protected endpoints  

Example header:Authorization: Bearer <your_access_token>

---

## ⚡ Installation

### 1️⃣ Clone Repository

git clone https://github.com/YOUR_USERNAME/smart_expense_tracker.git
cd smart_expense_tracker

### 2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate

### 3️⃣ Install Dependencies
pip install -r requirements.txt

### 4️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate

### 5️⃣ Create Superuser
python manage.py createsuperuser

### 6️⃣ Run Development Server
python manage.py runserver


🧠 Key Backend Concepts Demonstrated
	•	Custom User Model
	•	JWT Authentication
	•	Serializer Layer
	•	Permission Classes
	•	Foreign Key Relationships
	•	User-Level Data Isolation
	•	Secure API Design


🚀 Future Enhancements
	•	PostgreSQL Integration
	•	Docker Deployment
	•	AWS Hosting
	•	API Pagination
	•	Filtering & Search
	•	Budget Analytics
	•	CI/CD Pipeline

👨‍💻 Author

Harsh Patel

Aspiring Backend Engineer focused on building scalable and secure systems.
