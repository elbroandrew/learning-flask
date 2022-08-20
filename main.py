from flask import Flask, render_template, request, jsonify, g as app_ctx, redirect, session, make_response
import time

app = Flask(__name__)

@app.before_request
def start_time():
    app_ctx.start_time = time.perf_counter()

@app.after_request
def count_request_time(response):
    total_time = time.perf_counter() - app_ctx.start_time
    time_in_ms = int(total_time * 1000)
    return response

@app.route("/")
def index():
    time.sleep(1)
    return "Hello"


@app.route("/page1")
def page():
    res = make_response("SETTING a COOKIE")
    res.set_cookie('foo', 'bar', max_age=60*60)
    #session['my_text'] = 123
    #return f"{session.get('my_text')}"
    return res



if __name__ == '__main__':
    app.run(debug=True)
