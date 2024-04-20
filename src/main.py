from flask import *
from py_currency_converter import convert

app = Flask(__name__)

@app.route("/")
def index():
    currencies = {
        "USD" : convert(amount=1, to=['UAH'])
    }
    return render_template("index.html.j2", currencies = currencies)

if __name__ == '__main__':
    app.run()