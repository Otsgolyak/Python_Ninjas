from flask import Flask, request, render_template
import utils

app = Flask('app')


@app.route('/')
def root():
    return 'Hello'


@app.route('/now')
def now():
    return utils.time_now()


@app.route('/req')
def req():
    result = ''
    with open('./pyvenv.cfg') as f:
        result = f.read()
    result.replace('\n', '<br>')
    return result


@app.route('/gen_pass')
def gen_pass():
    length = int(request.args['length'])
    return utils.gen_password(length)


@app.route('/get_exchange_rate', methods=['GET', 'POST'])
def get_exchange():
    currency = request.form.get('curr')
    rate = utils.get_exchange_rate(currency)
    return render_template('btc.html', title='BTC', currency=currency, rate=rate)


@app.route('/table')
def table():
    fake_data = utils.fake_data()
    return render_template('table_bootstrap.html', title='Table', fake_data=fake_data)


@app.route('/astros')
def astros():
    astros = utils.astros()
    return render_template('astros.html', title='Astros', astros=astros)


@app.route('/csv')
def csv():
    return render_template('csv.html', title='CSV')
app.run(debug=True)
