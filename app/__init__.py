# Import the Flask Class from the flask module - will be main object
from flask import Flask
# Import SQLAlchemy and Migrate from their modules
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Import Config Class from confix module - will have all of the app's configurations
from config import Config



# Create and instance of the Flask Class called app
app = Flask(__name__)

# Create the app using the config class
app.config.from_object(Config)

#Create and instance of the SQLAlchemy to represent our database
db = SQLAlchemy(app)
#Create and instance of the Migrate to represent migration engine
migrate = Migrate(app, db)

# Import all of the routes and models from the routes and models files into the current folder
from . import routes, models


