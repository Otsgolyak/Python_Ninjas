import json
import os
import random
import sqlite3
import string
import datetime
import requests
from faker import Faker


def read_file(path):
    """
    ^_^
    :param path: the path to the file we need to read
    :return: string from the file
    """
    with open(path) as f:
        result = f.read()
    result.replace('\n', '<br>')
    return result


def get_requirements():
    """
    Very useful method, don't know what else to say...
    :return: requirements.txt
    """
    return read_file('./requirements.txt')


def gen_password(length=10):
    """
    Generates pass
    :param length: The length of pass
    :return: pass
    """
    return ''.join([
        random.choice(string.ascii_lowercase +
                      string.ascii_uppercase +
                      string.digits)
        for _ in range(length)
    ])


def time_now():
    """
    TIME MACHINE!
    :return: correct time
    """
    return datetime.datetime.strftime(datetime.datetime.now(), "%H:%M:%S")


def get_exchange_rate(currency):
    """
    Recieving the rate of BTC to currency from bitpay api
    :param currency: Takes the currency
    :return: the rate of BTC to currency
    """
    response = requests.get('https://bitpay.com/api/rates')
    resp_obj = json.loads(response.content)
    result = '<N/A>'
    for elem in resp_obj:
        if elem['code'] == currency:
            result = str(elem['rate'])
    return result


def fake_data():
    """
    Creates a list of fake users each time being called, using Faker lib
    :return: the list of fake users
    """
    fake = Faker()
    fake_list = [
        [idx, fake.name(), fake.email()]
        for idx, _ in enumerate(range(1, 101))
    ]
    return fake_list


def astros():
    """
    Using http://api.open-notify.org to collect the data about astronauts in space and their spacecrafts in Json
    :return: dict of astronauts in space
    """
    response = requests.get('http://api.open-notify.org/astros.json')
    result = json.loads(response.content)
    return result

def csv_reader():
    """
    Takes an CSV file and counts an average height and weight from it
    :return:rounded average height and weight
    """
    #TODO input file from frontend and add an attribute to count average
    import csv
    with open("students.csv", "r") as f:
        reader = csv.DictReader(f, delimiter=',')
        height = 0
        weight = 0
        count = 0
        for line in reader:
            count += 1
            height += float(line["height"])
            weight += float(line["weight"])
        return round(height/count), round(weight/count)


def execute_query(query):
    """
    Used to collect data from DB
    :param query: SQL query
    :return: List of data according to query
    """
    db_path = os.path.join(os.getcwd(), 'chinook.db')
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(query)
    records = cur.fetchall()
    return records

