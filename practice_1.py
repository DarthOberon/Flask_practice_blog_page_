from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy 
from forms import Resgistrationform, Loginform
app =Flask(__name__)


app.config['SECRET_KEY'] = '3dd13468875312d337e24a2350503cae'

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

@app.route("/register")
def register():
    form = Resgistrationform()
    return render_template('regster.html',title= 'Register',form=form)

@app.route("/login")
def login():
    form = Loginform()
    return render_template('login.html',title= 'Login',form=form)



if __name__ == "__main__":
    app.run(debug=True)