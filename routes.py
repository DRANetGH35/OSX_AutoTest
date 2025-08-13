from flask import render_template

from app import create_app
from forms import LossForm
from run import OSX

app = create_app()


@app.route('/')
def home():
    form = LossForm()
    return render_template('index.html', form=form, OSX=OSX)