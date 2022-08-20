from flask import Flask, render_template, request, jsonify, g as app_ctx, redirect
import time

app = Flask(__name__)

@app.before_request
def start_time():
    app_ctx.start_time = time.perf_counter()

@app.after_request
def count_request_time(response):
    total_time = time.perf_counter() - app_ctx.start_time
    time_in_ms = int(total_time * 1000)
    print(f"REQUEST TIME: {total_time}")
    return response

@app.route("/")
def index():
    time.sleep(1)
    return redirect("/page1", code=302)


@app.route("/page1")
def page():
    return "PAGE_1"



if __name__ == '__main__':
    app.run(debug=True)
