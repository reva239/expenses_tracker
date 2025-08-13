# app.py
from flask import Flask, request, jsonify, render_template
from datetime import datetime
from db import get_connection, init_db

app = Flask(__name__)

init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_expense():
    data = request.get_json()
    date = data.get("date", datetime.now().strftime("%Y-%m-%d"))
    category = data.get("category").lower()
    description = data.get("description", "")
    amount = data.get("amount")

    if not category or amount is None:
        return jsonify({"error": "Category and amount are required"}), 400

    with get_connection() as conn:
        conn.execute(
            "INSERT INTO expenses (date, category, description, amount) VALUES (?, ?, ?, ?)",
            (date, category, description, amount)
        )
    return jsonify({"message": "Expense added successfully"})

@app.route("/expenses", methods=["GET"])
def get_expenses():
    with get_connection() as conn:
        cursor = conn.execute("SELECT * FROM expenses ORDER BY date DESC")
        expenses = [
            {
                "id": row[0],
                "date": row[1],
                "category": row[2],
                "description": row[3],
                "amount": row[4]
            }
            for row in cursor.fetchall()
        ]
    return jsonify(expenses)

@app.route("/summary/<string:month>", methods=["GET"])
def monthly_summary(month):
    with get_connection() as conn:
        cursor = conn.execute("""
            SELECT category, SUM(amount)
            FROM expenses
            WHERE strftime('%Y-%m', date) = ?
            GROUP BY category
        """, (month,))
        summary = [
            {"category": row[0], "total": row[1]}
            for row in cursor.fetchall()
        ]
    return jsonify(summary)

if __name__ == "__main__":
    app.run(debug=True)
