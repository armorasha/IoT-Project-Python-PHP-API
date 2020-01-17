from sense_hat import SenseHat
from datetime import datetime

import random, time

import conn_py_math_db

sense = SenseHat()
sense.clear()

##sense.set_rotation(180)

blue = (0,0,255)
yellow = (255,255,0)
red = (255,0,0)
black = (0,0,0)
grey = (55,55,55)
white = (255,255,255)

counter = 0


# connecting to database and writing the sensor readings   
try:
   connection = conn_py_math_db.connect()

   dbhandler = connection.cursor()

   ### this is an infinite loop
   while True:

      counter += 1 # for executing mysql delete query once in 10 loops
   
      ### Step:1 Get sensor readings and process it------------
      temp_reading = sense.get_temperature()
      # temp_reading = random.uniform(4, 48)
      temperature = round(temp_reading, 2)

      pressure_reading = sense.get_pressure()
      # pressure_reading = random.uniform(900, 1100)
      pressure = round(pressure_reading, 2)

      humidity_reading = sense.get_humidity()
      # humidity_reading = random.uniform(0, 100)
      humidity = round(humidity_reading, 2)

      

      ### Step:2 Show output in Monitor------------
      message = "\nTemperature: " + str(temperature) + "C | Pressure: " + str(pressure) +\
       " millibars | Humidity: " + str(humidity) + "% \n"
      print(message)

      ### Step:3 Write sensor readings in database and keep only last 10 readings------------
      insert_sql_query = "INSERT INTO sensehat_readings (timestamp, temperature, pressure, humidity) VALUES (CONVERT_TZ(NOW(),'SYSTEM','Australia/Adelaide')" +\
             ', ' + str(temperature) + ', ' + str(pressure) + \
             ', ' + str(humidity) + ")"
      dbhandler.execute(insert_sql_query)

      if counter > 10:
         # keeping only 10 latest records in db and reset count
         delete_sql_query = "DELETE FROM sensehat_readings WHERE reading_id NOT IN(SELECT * FROM(SELECT reading_id FROM sensehat_readings ORDER BY timestamp DESC LIMIT 10) r)"
         dbhandler.execute(delete_sql_query)
         print ("Latest 10 records are kept in database and the rest are cleaned up")
         counter = 0
         
      # reading from db for testing
      # dbhandler.execute("SELECT * from sensehat_readings ORDER BY timestamp DESC") # Add LIMIT 1 if needed
      # result = dbhandler.fetchall()
      # for item in result:
      #   print(item)

      ### Step:4 Show output in Sensehat LEDs------------
      sensehat_message = str(round(temperature, 1)) + "C\n"
      sense.show_message(sensehat_message, text_colour = white, back_colour = black, scroll_speed = 0.03)


      ### Step:5 Wait 2 seconds and repeat------------
      #time.sleep(2)

      ### For Testing: Stopping infiniteloop after one execution------------
      # break
   
except Exception as e:
   print("Database connection Error: ")
   print(e)

finally:
   connection.close()



   
