from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    version = "1.0"
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f'Hello, World! Version: {version}, Current Time: {current_time}'

if __name__ == '__main__':
    app.run(port=8080)
