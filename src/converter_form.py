from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import DataRequired, Length, Regexp

class ConverterForm(FlaskForm):
    amount = FloatField('Сума', validators=[DataRequired(), Regexp(r"\d*")])
    fromCurrency = SelectField("З", choices=["USD", "UAH", "EUR"])
    toCurrency = SelectField("До",choices=["USD", "UAH", "EUR"])

