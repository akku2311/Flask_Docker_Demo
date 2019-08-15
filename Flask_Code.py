from flask import Flask

app = Flask(__name__)


# first endpoint #
@app.route('/')
def hello_world():
    return 'Flask Dockerized'


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
