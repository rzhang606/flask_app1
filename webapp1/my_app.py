from app import app

'''Flask Extensions:
 flask-wtf (forms)
 flask-sqlalchemy
 flask-migrate
'''
#remember to set FLASK_APP = my_app.py

'''
Flask-SQLAlchemy uses snake_case ( all lower, _ for space)
__tablename__ can be set to customize it

flask db init - creates migration repo for this application
flask db migrate - generates the migration script
flask db upgrade/downgrade - executes changes
'''

