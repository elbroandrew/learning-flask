from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/info')
def info():
    return "<h1>Puppies are cute</h1>"


@app.route('/info/<name>')
def puppy_name(name):
    return "<h1>This is {}</h1>".format(name)


if __name__ == '__main__':
    app.run(debug=True)
