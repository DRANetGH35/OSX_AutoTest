from flask import Flask
from datetime import timedelta
from sqlalchemy import select

from extensions import bootstrap

def create_app():
    app = Flask(__name__)

    with open('csrfkey.txt', 'r') as file:
        app.config['SECRET_KEY'] = file.readline().strip('\n')

    bootstrap.init_app(app)




    return app