import os

from flask import Flask, request, render_template, send_from_directory
import utils

app = Flask('app')


@app.route('/')
def index():
    return render_template('index.html')


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
    """
    HW with astronauts
    :return: template
    """
    astros = utils.astros()
    return render_template('astros.html', title='Astros', astros=astros)


@app.route('/csv')
def csv():
    """
    HW with CSV
    :return: template
    """
    av_height, av_weight = utils.csv_reader()
    return render_template('csv.html', title='CSV', av_height=av_height, av_weight=av_weight)


@app.route('/get-customers', methods=['GET', 'POST'])
def get_customers():
    """
    HW DB with customers
    :return: template
    """
    city = request.form.get('city')
    if not None:
        query = "SELECT * FROM customers WHERE City='{}';".format(city)
        records = utils.execute_query(query)
        result = render_template('get_customers.html', fake_data=records)
        return result


app.run(debug=True)
