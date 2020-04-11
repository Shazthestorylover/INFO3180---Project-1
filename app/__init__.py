from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Config Values
UPLOAD_FOLDER = './app/static/uploads/'


# Secret Key
SECRET_KEY = 'INFO3180_$3cretkey'

user = 'SHAZ'
password = 'Shaz1234'
database = 'INFO3180_Project_#01'
default = "postgresql://%s:%s@localhost/%s" % (user,password,database) 
#heroku = 'postgres://zajqwpbarejnhf:040063690ce3953033866218b60c4cf55f4836bffb741ee6cd8a6b8ac6f06bc3@ec2-34-193-232-231.compute-1.amazonaws.com:5432/d9endascgb7q21'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = default
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
app.config.from_object(__name__)
from app import views

#with app.app_context():
    #db.create_all()
