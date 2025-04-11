from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app =Flask(__name__)
app.config['SECRET_KEY'] = '3dd13468875312d337e24a2350503cae'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


from practice_1 import routes