from logging import error
from flask import Flask, request, make_response, redirect, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

toDos = ['buy coffe', 'Send mail', 'Go to the moon']


@app.errorhandler(404)
def not_found(err):
    return render_template('404.html', error=err, user_ip=request.remote_addr)


@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response


@app.route('/hello')
def hello():
    user_ip = request.remote_addr
    context = {
        'user_ip': user_ip,
        'toDos': toDos
    }

    return render_template('hello.html', **context)
