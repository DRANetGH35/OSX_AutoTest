from flask import render_template, request, redirect

from app import create_app
from forms import LossForm
from OSX import New_OSX

app = create_app()


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/connect')
def connect_osx():
    global osx
    global table
    table = []
    osx = New_OSX()
    return redirect('/test/ch1')

@app.route('/test/ch<int:ch>', methods=['GET', 'POST'])
def test(ch):
    form = LossForm()
    if request.method == 'GET':
        return render_template('test.html', form=form, OSX=osx, ch=ch)
    if request.method == 'POST':
        wave_a_loss = float(request.form.get('wave_a_loss'))
        wave_b_loss = float(request.form.get('wave_b_loss'))
        if wave_a_loss < .8 and wave_b_loss < .8:
            pass_state = "Pass"
        else:
            pass_state = "Fail"
        new_row = [ch, wave_a_loss, wave_b_loss, pass_state]
        table.append(new_row)
        ch += 1
        while ch <= osx.num_channel:
            return redirect(f'/test/ch{ch}')
        return 'success'
        print(table)