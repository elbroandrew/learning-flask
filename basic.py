import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)


app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# after app and db 
Migrate(app, db)

# Models
class Puppy(db.Model):

    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    # one to many
    # puppy to many toys
    toys = db.relationship('Toy', backref='puppy', lazy='dynamic')   # lazy - is how the data for relationship is loaded. Select - for separate tables load in two queries or more. Joined - to join tables in one query etc.
    # one to one
    # connect one puppy to one owner
    owner = db.relationship('Owner', backref='puppy', uselist=False)  # uselist is True by default.

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        if self.owner:
            return f"Puppy {self.name} and owner is {self.owner.name}."
        else:
            return f"Puppy {self.name} has no owner yet!"

    def report_toys(self):
        print(f"{self.name} toys: ")
        for toy in self.toys:
            print(toy.item_name)


class Toy(db.Model):
    __tablename__ = 'toys'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, item_name, puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id


class Owner(db.Model):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id



@app.route('/', methods=['GET','POST'])
def index():
    pass


if __name__ == '__main__':
    app.run(debug=True)