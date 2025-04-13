from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from dotenv import load_dotenv
import os

load_dotenv()
app =Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


from practice_1 import routes