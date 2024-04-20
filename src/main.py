from flask import *
from currency_converter import CurrencyConverter

c = CurrencyConverter()

app = Flask(__name__)

@app.route("/")
def index():
    currencies = {
        "USD" : c.convert(1, "USD", "EUR")
    }
    return render_template("index.html.j2", currencies = currencies)

if __name__ == '__main__':
    app.run()