from flask import *
app = Flask(__name__)

@app.route("/")
def index():
    nums = [1,2,3,4,5,6]
    return render_template("index.html", nums=nums)

if __name__ == '__main__':
    app.run()