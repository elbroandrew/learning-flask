from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"


@app.route('/info')
def info():
    return "<h1>Puppies are cute</h1>"


@app.route('/info/<name>')
def puppy_name(name):
    return "<h1>This is {}</h1>".format(name)


if __name__ == '__main__':
    app.run(debug=True)
