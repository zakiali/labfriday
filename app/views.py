from flask import render_template, flash, redirect, request, url_for
from app import app
from .forms import LoginForm

@app.route('/', methods=['GET','POST'])
def login():
    error = None
    form=LoginForm()
    if form.validate_on_submit():
        flash('Login requested for name="%s", email=%s, data=%s'%(form.name.data, form.email.data, str(form.date.data)))
        return redirect('success')
    return render_template('login.html',
                            title='Sign Up', 
                            form=form)

@app.route('/success', methods=['GET'])
def success():
    return render_template('success.html', title='Thank You')

