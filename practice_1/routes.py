from flask import render_template, url_for, flash, redirect
from practice_1 import app
from practice_1.forms import Resgistrationform, Loginform
from practice_1.models import db


posts =[
    {
        'author': 'Aryan Sharma',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'February 08, 2025'
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'February 09, 2025'
    
    }

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)
@app.route("/about")
def about():
    return render_template('about.html', title='About')



@app.route("/register",methods = ['GET','POST'])
def register():
    form = Resgistrationform()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}','success')
        return redirect(url_for('home'))
    return render_template('register.html',title= 'Register',form=form)

@app.route("/login",methods = ['GET','POST'])
def login():
    form = Loginform()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash('You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessfull! Please check Email and Password','danger')
    return render_template('login.html',title= 'Login',form=form)
