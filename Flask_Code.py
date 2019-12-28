from flask import Flask
from utility import sum_number
app = Flask(__name__)


# first endpoint #
@app.route('/')
def hello_world():
    print(1+2)
    input_list = list()
    for i in range(0, 10):
        input_list.append(i)
    print(input_list)
    sum_number(input_list)
    return 'Flask Dockerized'


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
