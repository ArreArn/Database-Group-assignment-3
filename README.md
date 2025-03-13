# 📚 Library Management System (LMS)

The **Library Management System (LMS)** is a Python-based desktop application built using **PyQt5** for the graphical
user interface (UI) and **PostgreSQL** as the backend database. This application helps users manage a library by keeping
track of books, members, and borrowing transactions.

The application follows a **three-layer architecture** for better modularity and maintainability.

---

## 🏛 Application Architecture

The project is structured based on the **three-layer architecture**, consisting of:

1. **UI Layer**:
    - Contains the graphical user interface built using **PyQt5**.
    - Responsible for handling user interaction and displaying data.

2. **Controller Layer**:
    - Acts as the bridge between the UI and the repository layer.
    - Contains the application’s business logic, processes user inputs, and interacts with the repository.

3. **Repository Layer**:
    - Handles data storage and retrieval using **PostgreSQL**.
    - Provides a clean interface for data operations (CRUD) on the database.

---

## 📋 Features

- Add, update, and delete books and members.
- Track borrowing and return history.
- Simple and intuitive PyQt5-based user interface.
- PostgreSQL database for persistent data storage.
- Modular architecture for scalability and easy maintenance.

---

## 🛠 Installation

### 1. Install Prerequisites

- Git
- Python 3.8 or higher
- PostgreSQL installed and configured
- Vscode or Pycharm

### 2. Clone this repository
First run the following command on your OS terminal

```bash
git clone https://github.com/Alirezalm/LMS_Project.git
```

Open the ```LMS_Project``` in vscode (or manually using or OS terminal)

### 3. Create and activate a virtual environment

#### 3.1 Using Command Line (Recommended on Linux and MacOS)

Run the following commands to create a virtual environment and activate it:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate

# On Linux/macOS
source venv/bin/activate
```

#### 3.2 Using Vscode Python Extension
Make sure Python Extension is installed on your Vscode.

Follow [this tutorial](https://code.visualstudio.com/docs/python/environments).

### 4. Install Python dependencies

After activating the virtual environment, install the required dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```
In this step you might get an error when installing psycopg2 package. In this case, you have to make sure
that PostgreSQL is installed correctly on your system. To manually install the dependencies run

```bash
pip install psycopg2
```

```bash
pip install pyqt5
```

```bash
pip install python-dotenv
```
### 5. Configure the PostgreSQL Database

Ensure that your PostgreSQL server is running and that you have created a database for the application. Update the
database connection settings in the repository layer to match your PostgreSQL configuration.

---
### 6. Create and Populate Tables

1. Create a database name "library" using PgAdmin.
2. Create tables in the library database by executing `tables.sql` script available in sql folder
3. Populate the created tables by executing 'populate.sql' script.

---


### 7. Running the Application
In this stage, in case you have done the previous steps correctly, the following command
will run the GUI of the application
```bash
python app.py
```

---



