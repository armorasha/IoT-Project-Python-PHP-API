import requests
import configparser

config = configparser.ConfigParser()
config.read('r_admin_use/db.ini')

client_key = config['math_mysql']['POST_KEY']

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

payload = {'temp': '14.99', 'pres': '1050.5', 'humi': '50.33', 'key': client_key}

# send the data in a POST request with 10 second timeout
# r = requests.post('http://localhost/php/data_receiver.php', data=payload, timeout=10)

r = requests.post('https://www.math.foodonya.com/iot/php/post_data_receiver.php',
                 data=payload, timeout=10, headers=headers)

print(r.text)
