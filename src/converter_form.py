from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import DataRequired, Length, Regexp

class ConverterForm(FlaskForm):
    amount = FloatField('Amount', validators=[DataRequired(), Regexp(r"\d*")])
    fromCurrency = SelectField("From", choices=["USD", "UAH", "EUR"])
    toCurrency = SelectField("To",choices=["USD", "UAH", "EUR"])

