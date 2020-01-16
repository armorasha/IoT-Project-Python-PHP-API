#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
#                                                          #
# Simple script to connect to a remote mysql database      #
#                                                          #
#                                                          #
# Install MySQLdb package by running:                      #
#                                                          #
#                       pip install MySQL-python           #
#                                                          #
########################################################

import mysql.connector

import configparser

config = configparser.ConfigParser()
config.read('../r_admin_use/db.ini')

HOST = config['math_mysql']['HOST']
USER = config['math_mysql']['USER']
PASSWORD = config['math_mysql']['PASSWORD']
DB = config['math_mysql']['DB']


try:
    conn = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DB
    )


    # print(conn) #for testing connection. returns a connection object.
    
    dbhandler = conn.cursor()
    dbhandler.execute("SELECT * from sensehat_readings")
    result = dbhandler.fetchall()
    for item in result:
        print(item)

except Exception as e:
    print("CONN ERROR: ")
    print(e)

finally:
    conn.close()
