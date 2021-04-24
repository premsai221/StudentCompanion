""" IMPORTING FROM pip installed modules """
from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user,logout_user,login_required
from threading import Thread
import time
from datetime import datetime


""" IMPORTING FROM STUDENTCOMAPANION PACKAGE """
from studentcompanion import app, bcrypt, db
from studentcompanion.forms import SignUpForm, LoginForm, TimeTableForm
from studentcompanion.models import User, Todo, Timetable, Reminders


"""
https://stackoverflow.com/questions/20652784/flask-back-button-returns-to-session-even-after-logout
https://flask-login.readthedocs.io/en/latest/#cookie-settings
https://flask-login.readthedocs.io/en/latest/#flask_login.LoginManager.header_loader
"""


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response



@app.route('/')
@app.route('/index')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    return render_template('index.html')



@app.route('/home')
@login_required
def home():
    return render_template('home.html',title='Home')



@app.route('/signup',methods=['GET','POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = SignUpForm()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User( name = form.name.data, email = form.email.data,number= form.number.data, password = hashed_pwd)
        db.session.add(user)
        db.session.commit()
        t_t = Timetable(user_id=user.id)
        db.session.add(t_t)
        db.session.commit()
        flash('Account successfully created. Now login with the credntials','primary')
        return redirect(url_for('login'))
    return render_template('signup.html', form = form, title='Signup')



@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            next_page = request.args.get('next').split('/') if request.args.get('next') else None
            return redirect(url_for(next_page[-1])) if next_page else redirect(url_for('home'))
        else:
            flash('Invalid Credentials','danger')
    return render_template('login.html',form=form, title='Login')



@app.route('/home/timetable')
@login_required
def timetable():
    tt_list = current_user.tt[0].time_table
    return render_template('timetable.html',tt_list=tt_list)



@app.route('/home/timetable/update_timetable',methods=['GET','POST'])
@login_required
def update_timetable():
    form = TimeTableForm()
    if form.is_submitted():
        l = []
        form_values_list = list(map(lambda x:x.data, list(form.__dict__.values())[4:-2]))
        for i in range(7):
            l.append(form_values_list[i*13:i*13+13])
        current_user.tt[0].time_table = l
        db.session.commit()
        return redirect(url_for('timetable'))


    temp = list(form.__dict__.values())[4:-2]
    form_list = []
    for i in range(7):
        form_list.append(temp[13*i:(13*i)+13])

    tt_list = current_user.tt[0].time_table

    for i,j in zip(form_list,tt_list):
        for p,q in zip(i,j):
            p.data = q

    return render_template('update_timetable.html',form=form,form_list=form_list)



@app.route('/home/todo')
@login_required
def todo():
    to_list = current_user.to_list
    return render_template('todo.html' ,to_list = to_list)



@app.route('/home/todo/add_add',methods=['GET','POST'])
@login_required
def add_todo():
    if request.method == 'POST' and request.form.get("toitem"):
        print(request.remote_addr)
        td = Todo(to_item = request.form.get("toitem"), user_id=current_user.id)
        db.session.add(td)
        db.session.commit()
    return redirect(url_for('todo'))



@app.route('/home/todo/todo_done',methods=['POST'])
@login_required
def todo_done():
    for id in request.form:
        td = Todo.query.get(id)
        td.done = True
        db.session.commit()
    return redirect(url_for('todo'))



@app.route('/home/todo/remove_todo',methods=['GET','POST'])
@login_required
def remove_todo():
    if request.method == 'POST':
        for name in request.form:
            td = Todo.query.get(int(name))
            db.session.delete(td)
            db.session.commit()
    return redirect(url_for('todo'))



@app.route('/home/reminder',methods=['GET','POST'])
@login_required
def reminder():
    date , time = str(datetime.now())[0:11], str(datetime.now())[11:16]
    remnds = Reminders.query.filter_by(user_id=current_user.id).order_by(Reminders.date_time).all()
    dt = [x.date_time.split()[0] for x in remnds]
    tm = [x.date_time.split()[1] for x in remnds]
    reminder_data = zip(remnds,dt,tm)
    return render_template('reminder.html',date=date,reminder_data=reminder_data)



@app.route('/home/reminder/add_reminder',methods=['GET','POST'])
@login_required
def add_reminder():
    date_time = request.form.get('date')+ ' ' +request.form.get('time')
    event = request.form.get('event')
    if request.method == 'POST' and date_time and event:
        if date_time > str(datetime.now())[:16] and event:
            rm = Reminders(user_id=current_user.id,event=event,date_time=date_time,number=current_user.number)
            db.session.add(rm)
            db.session.commit()
        else:
            flash('Reminder should be anytime later than now','info')
    return redirect(url_for('reminder'))



@app.route('/home/reminder/remove_reminder',methods=['POST'])
@login_required
def remove_reminder():
    for id in request.form:
        rem = Reminders.query.get(id)
        db.session.delete(rem)
        db.session.commit()
    return redirect(url_for('reminder'))



@app.route('/home/profile')
@login_required
def profile():
    return render_template('profile.html')



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
