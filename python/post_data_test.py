import requests

payload = {'temp': '30.33', 'pres': '1000.5', 'humi': '50.33'}

# send the data in a POST request with 10 second timeout
# r = requests.post('http://localhost/php/data_receiver.php', data=payload, timeout=10)

r = requests.get('https://math.foodonya.com/iot/php/data_receiver.php', params=payload, timeout=10)

print(r.url)

print(r.text)