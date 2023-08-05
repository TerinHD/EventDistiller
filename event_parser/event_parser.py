import os

from flask import Flask

app = Flask(__name__)
bind_port = int(os.environ['BIND_PORT'])


@app.route('/')
def hello():
    return "'Hello World!"

if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True, port=bind_port)
    