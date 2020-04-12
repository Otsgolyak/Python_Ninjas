import json
import random
import string
import datetime
import requests
from faker import Faker


def read_file(path):
    with open(path) as f:
        result = f.read()
    result.replace('\n', '<br>')
    return result


def get_requirements():
    return read_file('./requirements.txt')


def gen_password(length=10):
    return ''.join([
        random.choice(string.ascii_lowercase +
                      string.ascii_uppercase +
                      string.digits)
        for _ in range(length)
    ])


def time_now():
    return datetime.datetime.strftime(datetime.datetime.now(), "%H:%M:%S")


def get_exchange_rate(currency):
    response = requests.get('https://bitpay.com/api/rates')
    resp_obj = json.loads(response.content)
    result = '<N/A>'
    for elem in resp_obj:
        if elem['code'] == currency:
            result = str(elem['rate'])
    return result


def fake_data():
    fake_list = []
    counter = 0
    fake = Faker()
    for _ in range(100):
        name = fake.name()
        email = fake.email()
        counter += 1
        fake_list.append([counter, name, email])
    return fake_list


def astros():
    response = requests.get('http://api.open-notify.org/astros.json')
    result = json.loads(response.content)
    return result
