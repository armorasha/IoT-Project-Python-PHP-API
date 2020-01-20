from sense_hat import SenseHat
from datetime import datetime
import random, time
import sys

import urllib.request
import requests
import configparser


sense = SenseHat()
sense.clear()

##sense.set_rotation(180)

blue = (0,0,255)
yellow = (255,255,0)
red = (255,0,0)
black = (0,0,0)
grey = (55,55,55)
white = (255,255,255)
green = (0,255,0)
magenta = (255,0,255)
cyan = (0,255,255)


# FUNCTIONS--------------

#Prints in monitor and scrolls text in sensehat
def print_scroll_text(message, led_colour):
   print(message)
   sense.show_message(message, text_colour = led_colour, back_colour = black, scroll_speed = 0.03)

#Scrolls text in sensehat
def scroll_text(message, led_colour):
   sense.show_message(message, text_colour = led_colour, back_colour = black, scroll_speed = 0.03)


#Checks if internet is on by urlopen-ing google.com
def check_internet_status():
   try:
      urllib.request.urlopen('http://216.58.192.142', timeout=1)
      online_message = "\nInternet is on"
      print_scroll_text(online_message, green)
      return True
   except urllib.request.URLError as err:
      offline_message = "\nOFFLINE"
      print_scroll_text(offline_message, red)
      return False



#Get sensor readings
def get_sensor_readings():
   global temperature
   global pressure
   global humidity

   temp_reading = sense.get_temperature()
   # temp_reading = random.uniform(4, 48)
   temperature = round(temp_reading, 2)
   
   pressure_reading = sense.get_pressure()
   # pressure_reading = random.uniform(900, 1100)
   pressure = round(pressure_reading, 2)

   humidity_reading = sense.get_humidity()
   # humidity_reading = random.uniform(0, 100)
   humidity = round(humidity_reading, 2)

   #return temperature, pressure, humidity




#POSTs readings to db
def post_readings_to_db():
   try:
      screen_message = "\nTemperature: " + str(temperature) + "C | Pressure: " + str(pressure) +\
                " millibars | Humidity: " + str(humidity) + "%"

      sensehat_message = str(round(temperature, 1)) + "C"

      payload = {'temp': temperature, 'pres': pressure, 'humi': humidity, 'key': client_key}

      # send the data in a POST request with 10 second timeout
      # r = requests.post('http://localhost/php/data_receiver.php', data=payload, timeout=10)
      r = requests.post('https://www.math.foodonya.com/iot/php/data_receiver.php',
                 data=payload, timeout=10, headers=headers)

      # print(r.text) #For Testing: prints returned text sent by php echo statement

      # based on the text returned from POST request, auth success is checked here
      if (r.text == "POST data written to database after Auth"):       
         print(screen_message)
         scroll_text(sensehat_message, white)
         return True #return true if post successful
      elif (r.text == "POST Authentication failed"): 
         print_scroll_text(r.text, magenta)
         sys.exit() #exit if auth failed
            
   # exception raised for any reason
   except Exception as e:
      post_error = "\nPOST request failed: "
      print_scroll_text(post_error, red)
      print(e)
            
      reconnect_message = "\nWill attempt to reconnect...\n\n"
      print_scroll_text(reconnect_message, yellow)
      return False #return false if exception happen


#Cleans db and keep only last 10 records
def cleanup_db():   
   try:
      payload = {'key': client_key}

      # send the data in a POST request with 10 second timeout
      # r = requests.post('http://localhost/php/db_cleaner.php', data=payload, timeout=10)
      r = requests.post('https://www.math.foodonya.com/iot/php/db_cleaner.php',
        data=payload, timeout=10, headers=headers)

      # print(r.text) #For Testing: prints returned text sent by php echo statement

      # based on the text returned from POST request, auth success is checked here
      if (r.text == "Database cleaned after Auth"):            
         print("\nLatest 10 records are kept in database and the rest are cleaned up")
         scroll_text("Cleanup", blue)
         return True #return true if post successful
      elif (r.text == "POST Authentication failed"): 
         print_scroll_text(r.text, magenta)
         sys.exit()
   
   # exception raised for any reason
   except Exception as e:
      post_error = "\nPOST request failed: "
      print_scroll_text(post_error, red)
      print(e)
   
      reconnect_message = "\nWill attempt to reconnect...\n\n"
      print_scroll_text(reconnect_message, yellow)
      return False #return false if exception happen




# MAIN PROGRAM
if __name__ == '__main__':

    counter = 0

    # get client_key for POST request authentication on data_receiver.php from db.ini
    # other devices in the internet cannot POST data to my database without client_key
    # 'User-Agent' headers are to be sent with POST requests or my webserver is giving out 403 error
    config = configparser.ConfigParser()
    config.read('../r_admin_use/db.ini')
    client_key = config['math_mysql']['POST_KEY'] #get client key from db.ini
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    ### this is outer infinite loop
    while True:

      if not check_internet_status(): #if check_internet_status returns false
         continue #keep checking for internet by looping outer while loop


      ### this is inner infinite loop
      while True: # once internet is connected

         counter += 1 # counter for cleaning up db once in 10 loops

         ### Step:1 Get sensor readings
         get_sensor_readings()

         ### Step:2 POST sensor readings to web server
         # if can't, then break inner loop and go to outer loop
         if not post_readings_to_db(): # if post_readings_to_db returns false
            break    # break will close this inner loop and returns to outer loop where it checks internet status again

         
         ### Step:3 Keeping only 10 latest records in db and reset count
         if counter > 10:
            if not cleanup_db(): # if cleanup_db returns false
               break # break will close this inner loop and returns to outer loop where it checks internet status again
            else: # if cleanup_db returns true
               counter = 0 # reset counter
            





