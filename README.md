# 🚀 FastAPI + PostgreSQL Boilerplate with JWT Auth

![FastAPI Banner](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)

> A **production-ready FastAPI boilerplate** for rapid backend development — clean, secure, and developer-friendly.  
> This setup helps you jump-start new projects with best practices built-in.

---

## 🧩 Features

✅ **FastAPI** — lightning-fast web framework  
✅ **PostgreSQL + SQLAlchemy ORM** — relational database made simple  
✅ **JWT Authentication** — secure access tokens  
✅ **Password Hashing (bcrypt)** — strong encryption for user passwords  
✅ **Environment Variables** via `.env`  
✅ **Structured Modular Architecture** — easy to scale and maintain  
✅ **CRUD Example (User)** — Create, Read, Update, Delete  
✅ **Token-Based Login System**  
✅ **Interactive API Docs** — Swagger & ReDoc included  
✅ **Fully ready for local development**

---

## 🧱 Folder Structure

fastapi-auth-boilerplate/
│
├── app/
│ ├── core/
│ │ ├── config.py # Environment and settings
│ │ └── token.py # JWT token generation and verification
│ │
│ ├── db/
│ │ ├── database.py # Database connection setup
│ │ └── init_db.py # Database initialization (optional)
│ │
│ ├── models/
│ │ └── models.py # SQLAlchemy models (e.g., User)
│ │
│ ├── routes/
│ │ ├── auth.py # Authentication routes (login/register)
│ │ └── user.py # CRUD routes for users
│ │
│ ├── schemas/
│ │ └── schemas.py # Pydantic schemas for validation and serialization
│ │
│ ├── services/
│ │ ├── auth_service.py # Authentication business logic
│ │ └── user_service.py # User CRUD business logic
│ │
│ ├── utils/
│ │ ├── hash.py # Password hashing utilities (bcrypt)
│ │ └── init.py
│ │
│ ├── main.py # FastAPI application entry point
│ └── init.py
│
├── .env # Environment variables (local setup)
├── .env.sample # Example env file for reference
├── .gitignore # Git ignored files list
├── README.md # Project documentation
├── requirements.txt # Python dependencies
└── venv/ # Virtual environment (optional)

## ⚙️ Environment Variables (`.env`)

Create a file named `.env` in your project root and add the following:
DATABASE_URL=postgresql+psycopg2://postgres_username:postgres_password@localhost:5432/db_name
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60


> ⚠️ Make sure PostgreSQL is installed and running locally.

---

## 🧰 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/fastapi-postgres-boilerplate.git
cd fastapi-postgres-boilerplate

2️⃣ Create a Virtual Environment
python -m venv venv
source venv/bin/activate    # On macOS/Linux
venv\Scripts\activate       # On Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Set up the Database

Ensure PostgreSQL is running.

Create a new database (e.g., fastapi_boilerplate_db).

Update your .env file with the correct credentials.

Optionally initialize your tables:
python -m app.db.init_db

5️⃣ Run the Server
uvicorn app.main:app --reload

🚀 Running in Development Mode

FastAPI auto-reloads your app when files change:
uvicorn app.main:app --reload

then visit:

Swagger UI → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc

🧠 What's Inside?
| Component       | Description                                   |
| --------------- | --------------------------------------------- |
| **FastAPI**     | Modern, high-performance Python web framework |
| **PostgreSQL**  | Reliable open-source relational database      |
| **SQLAlchemy**  | ORM for database operations                   |
| **Pydantic**    | Data validation & serialization               |
| **bcrypt**      | Secure password hashing                       |
| **JWT (PyJWT)** | Token-based authentication                    |
| **dotenv**      | Loads environment variables from `.env`       |

🧪 Example API Endpoints
| Method   | Endpoint         | Description                    |
| -------- | ---------------- | ------------------------------ |
| `POST`   | `/auth/register` | Register new user              |
| `POST`   | `/auth/login`    | Login and get JWT token        |
| `GET`    | `/users/`        | Get all users (requires token) |
| `GET`    | `/users/{id}`    | Get user by ID                 |
| `PUT`    | `/users/{id}`    | Update user                    |
| `DELETE` | `/users/{id}`    | Delete user                    |

🧩 Development Tips

Use virtual environments for Python projects.

Keep your .env file private (add to .gitignore).

Use alembic for database migrations if needed.

Follow modular architecture for scalability

❤️ Author

Developed by CodeWithAzlo

If you like this boilerplate, don’t forget to ⭐ the repo!

!

🏁 License

This project is open-source and available under the MIT License.

---

Would you like me to also generate the **actual FastAPI folder and file code** (with models, routes, JWT auth, CRUD, etc.) so you can directly run this project locally and then push it to GitHub?



