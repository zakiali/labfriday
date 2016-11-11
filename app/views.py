from flask import render_template, flash, redirect, request, url_for, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from .forms import LoginForm, SignupForm
from .models import User

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/', methods=['GET','POST'])
def signup():
    form=SignupForm()
    if form.validate_on_submit():
        flash('Login requested for name="%s", email=%s, data=%s'%(form.name.data, form.email.data, str(form.date.data)))
        return redirect('success')
    return render_template('login.html',
                            title='Sign Up', 
                            form=form)

@app.route('/orderer', methods=['GET','POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('success'))
    form = LoginForm()


@app.route('/success', methods=['GET'])
def success():
    return render_template('success.html', title='Thank You')

