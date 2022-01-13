from flask import Flask, render_template, request

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


@app.route('/puppy/<name>')
def pup_name(name):
    return render_template('puppy.html', name=name)


@app.route('/signup_form')
def signup_form():
    return render_template('signup.html')

@app.route('/xss')
def xss_form():
    return render_template('xss-form.html')

@app.route('/xss_response')
def xss_response():
    first = request.args.get('first')
    return f"<div>{ first }</div>"


@app.route('/thank_you')
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')

    return render_template('thankyou.html', first=first, last=last)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
