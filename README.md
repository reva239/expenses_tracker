# 💰 Personal Expense Tracker (Flask + Bootstrap + Chart.js)

A simple web-based expense tracker built with **Python (Flask)** for the backend, **SQLite** for data storage, and **Bootstrap + Chart.js** for the frontend.  
This project allows users to **add expenses**, **view expense history**, and **see monthly spending summaries** with interactive charts.

---

## 🚀 Features
- **Add Expense**: Enter date, category, description, and amount.
- **View All Expenses**: Table view with latest expenses first.
- **Monthly Summary**: Interactive pie chart showing expenses per category.
- **Responsive UI**: Built with Bootstrap for mobile-friendly design.
- **Lightweight Database**: Uses SQLite (no extra setup required).

---

## 🛠 Tech Stack
**Backend**  
- Python 3.x  
- Flask 3.0.3  
- SQLite (built-in with Python)  

**Frontend**  
- HTML5, CSS3, JavaScript  
- Bootstrap 5 (for styling)  
- Chart.js (for interactive charts)  

---

## 📂 Project Structure
expense_tracker/
│── app.py # Main Flask application
│── db.py # Database connection & setup
│── requirements.txt # Python dependencies
│── expenses.db # SQLite database (auto-created on first run)
│── templates/
│ └── index.html # Frontend HTML template

---

## ⚙️ Installation & Setup

### 1. Clone this repository
```bash
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
python -m venv venv
source venv/bin/activate   # For Mac/Linux
venv\Scripts\activate      # For Windows
pip install -r requirements.txt
python app.py
```
---

## 📄 Project Description (Click to Copy)
<span style="pointer:courser'" onclick="()=>navigator.clipboard.writeText(this.innerText)">
This Personal Expense Tracker is a full-stack web application designed to help users record, manage, and analyze their daily expenses. The backend is built with Python’s Flask framework, handling all data operations and providing REST API endpoints for adding, retrieving, and summarizing expenses. SQLite is used as the database to keep the project lightweight and easy to run without additional configuration.

The frontend is developed using HTML, Bootstrap for responsive styling, and Chart.js for interactive data visualization. Users can easily add expenses by specifying the date, category, description, and amount. The expenses are displayed in a clean, sortable table. A monthly summary view allows users to select a month and see category-wise spending in an interactive pie chart, making it easy to identify spending patterns.

This project demonstrates skills in full-stack development, REST API design, frontend-backend communication via fetch API, and integrating data visualization libraries. It is beginner-friendly, runs locally without complex setup, and is suitable for inclusion in a developer portfolio. It showcases essential development concepts such as CRUD operations, responsive UI design, and dynamic chart rendering.

Clicking this box will copy this description to your clipboard, making it quick to paste into resumes, reports, or documentation.
</span>



