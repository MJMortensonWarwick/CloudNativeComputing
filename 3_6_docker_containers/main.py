import os
from flask import Flask
from random import randint

app = Flask(__name__)


@app.route('/')
def hello_world():
    names = {1: "Mark", 2: "Liping", 3: "Jordan", 4: "Michael"}
    name = names[randint(1, 4)]
    return f"{name} says Hello 👋"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))

