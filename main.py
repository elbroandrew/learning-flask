from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"


@app.route('/info')
def info():
    return "<h1>Puppies are cute</h1>"

if __name__ == '__main__':
    app.run()
