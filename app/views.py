from flask import render_template, flash, redirect, request, url_for, g
from app import app, db
from .forms import SignupForm, RestaurantForm, FoodForm
from .models import User, Lunches
import datetime

def gen_last_n_orders(n=4):
    recents = []
    for lunch in Lunches.query.order_by(Lunches.datestamp.desc()).all()[:n]:
        recents.append(dict(zip(('date', 'name', 'restaurant'),(lunch.datestamp, lunch.author.nickname, lunch.restaurant))))
    return recents

def get_taken_dates():
    takendates = []
    for lunch in Lunches.query.order_by(Lunches.datestamp.desc()).all():
        takendates.append(lunch.datestamp.strftime('%d-%m-%Y'))
    return takendates

def get_next_volunteer():
    '''Get the volunteer for tomorrow.'''
    today = datetime.date.today()# get today's date
    nextfriday = (today + datetime.timedelta( (4 - today.weekday()) %7 ) ).toordinal()
    whosdict = {}
    for lunch in Lunches.query.order_by(Lunches.datestamp.desc()).all():
        whosdict[nextfriday - lunch.datestamp.toordinal()] = lunch
    try:
        return whosdict[1]
    except KeyError:
        return None

def get_todays_volunteer():
    '''Get todays volunteer.'''
    today = datetime.date.today()# get today's date
    whosdict = {}
    for lunch in Lunches.query.order_by('datestamp desc').all():    
        whosdict[today.toordinal() - lunch.datestamp.toordinal()] = lunch
    try:
        return whosdict[0]
    except KeyError:
        return None

def get_restaurants():
    restaurants = []
    for lunch in Lunches.query.order_by(Lunches.restaurant):
        restaurants.append(lunch.restaurant)
        
def add_restaurant(date, restaurant):
    for r in Lunches.query.order_by(Lunches.datestamp):
        if date == r.datestamp.strftime('%Y-%m-%d'): 
            print date, r.datestamp
            print restaurant
            r.restaurant = restaurant
            db.session.commit()
            break
    return r

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
        #flash('Login requested for name="%s", email=%s, date=%s'%(name, email, date))
        add_user_to_db(name, email, date)
        
        return redirect(url_for('success',name=name, date=date))
    return render_template('login.html',
                            title='Sign Up', 
                            form=form,
                            recents=gen_last_n_orders(n=8),
                            takendates=get_taken_dates())

@app.route('/success/<name>/<date>', methods=['GET','POST'])
def success(name,date):
    form = RestaurantForm()
    if form.validate_on_submit():
        restaurant = form.restaurant.data
        lunch = add_restaurant(date, restaurant)
        flash('restaurant record has been updated with value {0}'.format(lunch.restaurant))
    return render_template('success.html', 
                          title='Thank You',
                          form=form,
                          recents=gen_last_n_orders(n=8),
                          name=name)

