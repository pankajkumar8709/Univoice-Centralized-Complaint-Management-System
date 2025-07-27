from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///complaint.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'pankaj'
db=SQLAlchemy(app)


# Setup database engine
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/mk538/OneDrive/Desktop/Cursor/system/mycollege.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/mk538/OneDrive/Desktop/Cursor/system/portal/mycollege.db'

engine = create_engine('sqlite:///C:/Users/mk538/OneDrive/Desktop/Cursor/system/portal/mycollege.db')
metadata = MetaData()
metadata.reflect(bind=engine)

# Reflect existing tables
students = metadata.tables['students']
teachers = metadata.tables['teachers']
admins = metadata.tables['admins']

from portal import routes  # Import routes last


