from flask_wtf import FlaskForm
from flask_wtf.form import _Auto
from wtforms import StringField, FloatField, SelectField, SubmitField, Label
from wtforms.validators import DataRequired, Length, Regexp
from py_currency_converter.py_exchange_rate import country_codes

class ConverterForm(FlaskForm):
    amount = FloatField('Сума', validators=[DataRequired(), Regexp(r"\d*")])
    fromCurrency = SelectField("З  ", choices=country_codes)
    toCurrency = SelectField("До",choices=country_codes)
    result = Label("res", "Результат: ")
    submit = SubmitField("Конвертувати")

