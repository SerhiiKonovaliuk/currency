from flask import *
from py_currency_converter import convert
from converter_form import ConverterForm
from flask_wtf.csrf import CSRFProtect
import os
SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect(app)

@app.route("/", methods=['GET', 'POST'])
def get_index():
    currencies = {
        "USD" : convert(base="USD", amount=1, to=['UAH'])["UAH"],
        "EUR" : convert(base="EUR", amount=1, to=['UAH'])["UAH"],
        "PLN" : convert(base="PLN", amount=1, to=['UAH'])["UAH"]
    }
    form = ConverterForm()
    base = request.form.get("fromCurrency")
    amount = request.form.get("amount")
    to = request.form.get("toCurrency")
    if base != None and amount != None and to != None:
        converted = convert(base=base, amount=int(amount), to=[to])[to]
        form.result = "{:.2f}".format(converted)
    return render_template("index.html", currencies = currencies, form = form)
if __name__ == '__main__':
    app.run()