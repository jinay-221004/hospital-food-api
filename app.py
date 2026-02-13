# import pyodbc
from flask import Flask, render_template, request
import pyodbc
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    food = request.form["food"]

    conn = pyodbc.connect(os.environ["DB_CONNECTION"])
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO Orders (PatientName, FoodItem) VALUES (?, ?)",
        (name, food)
    )

    conn.commit()
    conn.close()

    return "Order Added Successfully!"

if __name__ == "__main__":
    app.run()


