from flask import render_template, flash, redirect, request, url_for
from app import app
from .forms import LoginForm

@app.route('/', methods=['GET'])
#@app.route('/index', methods=['GET'])
def index():
    return redirect('/login')

@app.route('/login', methods=['GET','POST'])
def login():
    next = request.form.get('next')
    if next is None:
        next=url_for('index')
    form=LoginForm()
    if form.validate_on_submit():
        flash('Login requested for name="%s", data=%s'%(form.name.data, str(form.date.data)))
        return redirect('success')
    return render_template('index.html',
                            title='Sign Up', 
                            form=form)

@app.route('/success', methods=['GET'])
def success():
    return render_template('success.html', title='Thank You')

