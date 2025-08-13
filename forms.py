from wtforms.fields import PasswordField, SubmitField, StringField, IntegerField
from wtforms.fields.choices import SelectField
from wtforms.fields.numeric import FloatField
from wtforms.fields.simple import BooleanField
from wtforms.validators import DataRequired, ValidationError
from flask_wtf import FlaskForm
from werkzeug.security import check_password_hash, generate_password_hash

def ensure_positive_number(form, field):
    print(field.data)
    if field.data < 0:
        raise ValidationError('Enter a positive number')

class LossForm(FlaskForm):
    wave_a_loss = FloatField('Wave A Loss', validators=[DataRequired(), ensure_positive_number])
    wave_b_loss = FloatField('Wave B Loss', validators=[DataRequired(), ensure_positive_number])

    submit = SubmitField('Submit', render_kw={'class': 'btn custom-btn'})