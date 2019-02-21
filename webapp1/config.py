import os

#configure db named app.db located in main directory of application (stored in this variable)
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'app.db')

    #signals application every time change is about to made in db
    SQLALCHEMY_TRACK_MODIFICATIONS = False
