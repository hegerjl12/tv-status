from flask import Flask, request, abort, render_template, url_for, flash, redirect
from deta import Deta


deta = Deta('b0bjxtd6_PyvkvLdwfvHVm7k7MccimkFX1H3K3ZMr')
db = deta.Base('SPY')

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return "Home Page"

@app.route('/spy_webook', methods=['POST'])
def spy_webhook():
    if request.method == 'POST':

        data = request.json

        alert_timeframe = data['timeframe']
        alert_direction = data['signal']
        alert_price = data['price']

        db.put({
            "signal": alert_direction, "price": alert_price
        })

        return 'success', 200
    else:
        abort(400)


