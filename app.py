from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hospital Food App is Working!"

if __name__ == "__main__":
    app.run()
