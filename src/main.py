from flask import *
from py_currency_converter import convert
from converter_form import ConverterForm
from flask_wtf.csrf import CSRFProtect
import os
SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect(app)

@app.route("/")
def index():
    currencies = {
        "USD" : convert(base="USD", amount=1, to=['UAH'])["UAH"],
        "EUR" : convert(base="EUR", amount=1, to=['UAH'])["UAH"],
        "PLN" : convert(base="PLN", amount=1, to=['UAH'])["UAH"]
    }
    return render_template("index.html.j2", currencies = currencies, form = ConverterForm())

if __name__ == '__main__':
    app.run()