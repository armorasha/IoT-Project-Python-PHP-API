import requests

payload = {'temp': '30.33', 'pres': '1000.3', 'humi': '50.33'}

# send the data in a POST request with 10 second timeout
r = requests.post('http://localhost/php/data_receiver.php',
                  data=payload, timeout=10)
