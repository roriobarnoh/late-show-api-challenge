# 🎤 Late Night TV Show API

A Flask-based RESTful API for managing a Late Night TV Show system, with support for managing users, guests, episodes, and guest appearances. Designed with PostgreSQL, SQLAlchemy ORM, and JWT authentication.

---

## 📦 Features

- ✅ User registration & JWT-based login
- 🎙️ CRUD for Guests, Episodes, and Appearances
- 🎥 Guests can appear in multiple episodes (Many-to-Many)
- 🔐 Protected endpoints for authenticated actions
- 🔄 Cascading deletes for appearances
- 🧪 API tested using Postman

---

## 🛠️ Tech Stack

- **Backend**: Flask, Flask-RESTful, Flask-Migrate, Flask-JWT-Extended
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Migrations**: Alembic via Flask-Migrate
- **Testing**: Postman
- **Authentication**: JWT (JSON Web Tokens)

---

## 📁 Project Structure
late_show_api/
├── app/
│ ├── init.py
│ ├── models.py
│ ├── routes.py
│ ├── auth.py
│ └── utils.py
├── migrations/
├── seed.py
├── config.py
├── app.py
├── requirements.txt
└── README.md


---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/late-show-api.git
cd late-show-api

### 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Setup PostgreSQL database
Create a PostgreSQL database:
createdb late_show_db

### 5. Configure environment variables
Create a .env file or export variables:
export FLASK_APP=app
export FLASK_ENV=development
export DATABASE_URL=postgresql://<username>:<password>@localhost/late_show_db
export JWT_SECRET_KEY=your_secret_key

### 6. Initialize database
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

### 7. Seed the database
python seed.py

### 8. Run the server
flask run



