import unittest
from flask import request, make_response, redirect, render_template, session, url_for, flash
from flask_login import login_required

from app import create_app
from app.forms import LoginForm
from app.firestore_service import get_users, get_todos

app = create_app()

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')# carpeta test
    unittest.TextTestRunner().run(tests)# run tests

@app.errorhandler(500)
def server_error(error):
    return render_template('505.html',error=error)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html',error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr #pide la ip
    response = make_response(redirect('/hello'))# genera la respuesta
    session['user_ip'] = user_ip #la guarda en modo cookie

    return response

@app.route('/hello', methods=['GET'])
@login_required
def hello():
    #se crean las instancias
    user_ip=session.get('user_ip')
    username =session.get('username')# obtenemos el user de la sesion
    context = { #! Diccionario de python | para variables q estan en el tamplate
        'user_ip': user_ip,
        'todos': get_todos(user_id=username),
        'username': username
    }

    return render_template('hello.html', **context)#TODO: ** Expande todas las variables


