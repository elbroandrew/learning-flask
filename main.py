from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    user_logged_in = True
    return render_template('index.html', user_logged_in=user_logged_in)


@app.route('/info')
def info():
    return "<h1>Puppies are cute</h1>"


@app.route('/info/<name>')
def puppy_name(name):
    return "<h1>This is {}</h1>".format(name)


if __name__ == '__main__':
    app.run(debug=True)
