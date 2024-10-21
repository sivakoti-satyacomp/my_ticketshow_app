#Starting of the app
from flask import Flask
from backend.models import db


app=None

def setup_app():
    app=Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///ticket_show.sqlite3" #Having db file
    db.init_app(app) #Flask app connected to db(SQL alchemy)
    app.app_context().push() #Direct access to other modules
    app.debug=True
    print("Ticket Show app is started...")



#Call the setup
setup_app()

from backend.controllers import *

if __name__=="__main__":
    app.run()