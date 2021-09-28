from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

toDos = ['buy coffe', 'Send mail', 'Go to the moon']


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
