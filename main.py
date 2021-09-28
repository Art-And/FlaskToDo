from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)


@app.route('/hello')
def hello():
    user_ip = request.remote_addr

    return render_template('hello.html', user_ip=user_ip)


@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response
