import mysql.connector

import configparser

config = configparser.ConfigParser()
config.read('r_admin_use/db.ini')

HOST = config['math_mysql']['HOST']
USER = config['math_mysql']['USER']
PASSWORD = config['math_mysql']['PASSWORD']
DB = config['math_mysql']['DB']

def connect():
    return mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DB
    )
