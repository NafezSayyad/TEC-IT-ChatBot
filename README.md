# TEC-IT ChatBot

This project aims to build a backend-only AI chatbot for TEC-IT customer support using:
- LangChain for orchestration
- FAISS for vector storage
- OpenAI for LLMs
- Docker for containerization



# Project Setup Guide

This guide will help you set up and run the project from scratch using Python virtual environments, an `.env` file, and Visual Studio Code.

---

## 🚀 Getting Started

### 1️⃣ Prerequisites

Ensure you have the following installed on your system:

- **Python 3.8+** ([Download Here](https://www.python.org/downloads/))
- **pip** (comes with Python, but update it using `pip install --upgrade pip`)
- **Visual Studio Code** ([Download Here](https://code.visualstudio.com/))
- **VS Code Extensions:**
  - Python Extension (install from VS Code Marketplace)
  - `.env` support (optional)

---

## 🏗️ Setup Steps

### 2️⃣ Clone the Repository

```sh
git clone https://github.com/your-repo/project-name.git
cd project-name
```

---

### 3️⃣ Create a Virtual Environment

#### On Windows (CMD/PowerShell)
```sh
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux
```sh
python3 -m venv venv
source venv/bin/activate
```

> ✅ The virtual environment is now activated. You should see `(venv)` in your terminal.

---

### 4️⃣ Create an `.env` File

Inside the root directory, create a **.env** file and add the following:

```ini
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
DEBUG=True
```

> ✅ Update values accordingly based on your project requirements.

---

### 5️⃣ Install Dependencies

Run the following command to install required dependencies from `requirements.txt`:

```sh
pip install -r requirements.txt
```

If your project uses additional dependencies, install them manually:

```sh
pip install <package-name>
```

To update `requirements.txt` after installing new packages:

```sh
pip freeze > requirements.txt
```

---

### 6️⃣ Open Project in VS Code

1. Open **VS Code**.
2. Click **File → Open Folder** and select the project folder.
3. Open the command palette (`Ctrl + Shift + P` on Windows/Linux, `Cmd + Shift + P` on macOS).
4. Search for **"Python: Select Interpreter"** and choose the one inside your `venv` folder.

---

### 7️⃣ Running the Project

To run the project, execute:

```sh
python main.py
```

Or, if using Django/Flask:

```sh
python manage.py runserver
```

For FastAPI:

```sh
uvicorn main:app --reload
```

---

### 8️⃣ Deactivating Virtual Environment

Once you're done, deactivate the virtual environment using:

```sh
deactivate  # macOS/Linux
venv\Scripts\deactivate  # Windows
```

---

## ✅ Additional Notes

- If you face permission issues on Linux/macOS, try `chmod +x venv/bin/activate`.
- For database setup, update `DATABASE_URL` in `.env` accordingly.
- Consider using a **.gitignore** file to exclude unnecessary files, including `venv/` and `.env`.

---

## 📌 Common Issues & Fixes

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` again |
| Virtual environment not found | Ensure you activated it with `source venv/bin/activate` |
| `Permission denied` | Try running commands with `sudo` (macOS/Linux) |

---

🎉 **You're all set!** 🚀 Now you can start coding and building your project. Happy coding! 😃
