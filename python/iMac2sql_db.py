#from sense_hat import SenseHat
from datetime import datetime

import random, time

import conn_py_math_db

# sense = SenseHat()
# sense.clear()

##sense.set_rotation(180)

blue = (0,0,255)
yellow = (255,255,0)
red = (255,0,0)
black = (0,0,0)
grey = (55,55,55)
white = (255,255,255)


### this is an infinite loop
while True:
   ### Step:1 Get sensor readings and process it------------
   # temp_reading = sense.get_temperature()
   temp_reading = random.uniform(4, 48)
   temperature = round(temp_reading, 1)

   # pressure_reading = sense.get_pressure()
   pressure_reading = random.uniform(900, 1100)
   pressure = int(pressure_reading)

   # humidity_reading = sense.get_humidity()
   humidity_reading = random.uniform(0, 100)
   humidity = int(humidity_reading)

   

   ### Step:2 Show output in Monitor------------
   message = "\nTemperature: " + str(temperature) + "C | Pressure: " + str(pressure) +\
    " millibars | Humidity: " + str(humidity) + "% \n"
   print(message)


   ### Step:3 Write sensor readings in database and keep only last 10 readings------------
   try:
      connection = conn_py_math_db.connect()

      dbhandler = connection.cursor()
      
      # writing to db
      insert_sql_query = "INSERT INTO sensehat_readings (timestamp, temperature, pressure, humidity) VALUES (NOW()" +\
          ', ' + str(temperature) + ', ' + str(pressure) + \
          ', ' + str(humidity) + ")"
      dbhandler.execute(insert_sql_query)

      # keeping only 10 latest records in db
      delete_sql_query = "DELETE FROM sensehat_readings WHERE reading_id NOT IN(SELECT * FROM(SELECT reading_id FROM sensehat_readings ORDER BY timestamp DESC LIMIT 10) r)"
      dbhandler.execute(delete_sql_query)
      
      # reading from db
      dbhandler.execute("SELECT * from sensehat_readings ORDER BY timestamp DESC LIMIT 1")
      result = dbhandler.fetchall()
      for item in result:
         print(item)
   
   except Exception as e:
      print("Database connection Error: ")
      print(e)

   finally:
      connection.close()




   ### Step:4 Show output in Sensehat LEDs------------
   # sense.show_message(message, text_colour = white, back_colour = black, scroll_speed = 0.1)


   ### Step:5 Wait 2 seconds and repeat------------
   #time.sleep(2)

   ### For Testing: Stopping infiniteloop after one execution------------
   break