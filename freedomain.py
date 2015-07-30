from flask import Flask

app = Flask(__name__)


@app.route('/')
def start(count):
    return 'SETUP APP'


if __name__ == '__main__':
    app.run(host="172.31.27.41", port=8080)