from flask import render_template, request

from app import create_app
from forms import LossForm
from OSX import New_OSX

app = create_app()


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    osx = New_OSX()
    i = 1
    form = LossForm()

    if request.method == 'GET':
        return render_template('test.html', form=form, OSX=osx, i=i)
    if request.method == 'POST':
        while i <= osx.num_channel:
            i += 1
            return render_template('test.html', form=form, OSX=osx, i=i)
