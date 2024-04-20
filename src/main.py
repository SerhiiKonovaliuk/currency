from flask import *
from py_currency_converter import convert

app = Flask(__name__)

@app.route("/")
def index():
    currencies = {
        "USD" : convert(base="USD", amount=1, to=['UAH'])["UAH"],
        "EUR" : convert(base="EUR", amount=1, to=['UAH'])["UAH"],
        "PLN" : convert(base="PLN", amount=1, to=['UAH'])["UAH"]
    }
    return render_template("index.html.j2", currencies = currencies)

if __name__ == '__main__':
    app.run()