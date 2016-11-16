from flask import render_template, flash, redirect, request, url_for, g
from app import app, db
from .forms import LoginForm, SignupForm
from .models import User, Lunches

def gen_last_n_orders(n=4):
    recents = []
    for lunch in Lunches.query.order_by('datestamp desc').all()[:n]:
        recents.append(dict(zip(('date', 'name', 'restaurant'),(lunch.datestamp, lunch.author.nickname, lunch.restaurant))))
    return recents

def get_taken_dates():
    takendates = []
    for lunch in Lunches.query.order_by('datestamp desc').all():
        print lunch.datestamp
        takendates.append(lunch.datestamp.strftime('%d-%m-%Y'))
    print takendates
    return takendates
        

def add_user_to_db(name, email, date):
    #check to see if in data base already by using email.
    user = User.query.filter_by(email=email).first()
    if user == None:
        #if not in db, add user and lunch session
        user = User(nickname=name, email=email)
        db.session.add(user)
        l = Lunches(datestamp=date, author=user)
        db.session.add(l)
    else: 
        #if user in db, add lunch with author as user
        l = Lunches(datestamp=date, author=user)
        db.session.add(l)
    db.session.commit()
    return None
    

@app.route('/', methods=['GET','POST'])
def signup():
    #get persons name who is ordering lab friday lunch this week
    form=SignupForm()
    if form.validate_on_submit():
        name, email, date = form.name.data, form.email.data, form.date.data
        flash('Login requested for name="%s", email=%s, date=%s'%(name, email, date))
        add_user_to_db(name, email, date)
        return redirect('success')
    return render_template('login.html',
                            title='Sign Up', 
                            form=form,
                            recents=gen_last_n_orders(),
                            #takendates=get_taken_dates())
                            takendates=['02-12-2016', '18-11-2016', '11-11-2016', '04-11-2016', '12-09-2016', '01-01-2016'])

@app.route('/success', methods=['GET'])
def success():
    form = LoginForm()
    return render_template('success.html', 
                          title='Thank You',
                          recents=gen_last_n_orders())


#@app.route('/user/<nickname>')
