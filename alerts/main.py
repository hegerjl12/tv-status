from flask import Flask, request, abort, render_template, url_for, flash, redirect
from deta import Deta

app = Flask(__name__)

deta = Deta('b0hip04s_76Lucyw7JK6pt3vKtpD4kUmZZfQKfuwo')
spy15m_db = deta.Base('SPY15m')
spy1m_db = deta.Base('SPY1m')



@app.route('/', methods=["GET"])
def index():
    return  "Home Page"

@app.route('/spy_webhook', methods=['POST'])
def spy_webhook():
    if request.method == 'POST':

        data = request.json

        alert_timeframe = data['timeframe']
        alert_direction = data['signal']
        alert_price = data['price']
        
        if alert_timeframe == '1m':
            spy1m_db.put(
                {"signal": alert_direction, "price": alert_price},
                'current' )

        if alert_timeframe == '15m':
            spy15m_db.put(
                {"signal": alert_direction, "price": alert_price},
                'current' )

        return 'success', 200
    else:
        abort(400)


