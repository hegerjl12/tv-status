from flask import Flask, request, abort, render_template, url_for, flash, redirect
from deta import Deta

app = Flask(__name__)

deta = Deta('b0xrzj95_36AvMwmWFKZuzkk4sZmA3wki6VrAQHNG')
db = deta.Base('SPY')

test = False

@app.route('/', methods=["GET"])
def index():
    if test:
        return "Home Page True"
    else:
        return  "Home Page False"

@app.route('/spy_webook', methods=['POST'])
def spy_webhook():
    if request.method == 'POST':

        data = request.json

        alert_timeframe = data['timeframe']
        alert_direction = data['signal']
        alert_price = data['price']
        test = True
        db.put({
            "signal": alert_direction, "price": alert_price
        })

        return 'success', 200
    else:
        abort(400)


