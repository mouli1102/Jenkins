from flask import Flask
app = Flask(__name__)

@app.route("/")
def return_int_value():
    return "22"

if __name__ == "__main__":
    app.run(host="localhost", port=int(5009))
