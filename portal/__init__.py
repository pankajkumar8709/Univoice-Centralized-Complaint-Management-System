from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData

from flask_migrate import Migrate

migrate = Migrate()


app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///newcomplaint.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'pankaj'
db=SQLAlchemy(app)


# Setup database engine
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/mk538/OneDrive/Desktop/Cursor/system/mycollege.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/mk538/OneDrive/Desktop/Cursor/system/portal/newmycollege.db'

engine = create_engine('sqlite:///C:/Users/mk538/OneDrive/Desktop/Cursor/system/portal/newmycollege.db')
metadata = MetaData()
metadata.reflect(bind=engine)

# Reflect existing tables
students = metadata.tables['students']
teachers = metadata.tables['teachers']
admins = metadata.tables['admins']


migrate.init_app(app, db)
from portal import routes  # Import routes last


