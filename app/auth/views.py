from flask import render_template,redirect, render_template, session, url_for, flash
from . import auth
from app.forms import LoginForm


@auth.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }
    #**agregar el username en la sesion
    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username# guardamos el username en la sesion

        #Flash (mensaje de alerta )
        flash('nombre de usuario registrado con exito!')
        return redirect(url_for('index'))

    return render_template('login.html', **context)