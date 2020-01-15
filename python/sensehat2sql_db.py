#from sense_hat import SenseHat
from datetime import datetime

import random, time

import conn_math_db

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
   # temp = sense.get_temperature()
   temp = random.uniform(1, 58)
   t= round(temp,1)


   ### Step:2 Write sensor readings in database and keep only last 10 readings------------
   try:
      connection = conn_math_db.connect()

      dbhandler = connection.cursor()
      
      # writing to db
      insert_sql_query = "INSERT INTO sensehat_readings (timestamp, temperature) VALUES (NOW()" + ', ' + str(t) + ");"
      dbhandler.execute(insert_sql_query)

      # keeping only 10 records in db
      delete_sql_query = "DELETE FROM sensehat_readings WHERE reading_id NOT IN(SELECT * FROM(SELECT reading_id FROM sensehat_readings ORDER BY timestamp DESC LIMIT 3) r)"
      dbhandler.execute(delete_sql_query)
      
      # reading from db
      dbhandler.execute(
          "SELECT * from sensehat_readings ORDER BY timestamp DESC")
      result = dbhandler.fetchall()
      for item in result:
         print(item)
   
   except Exception as e:
      print("Database connection Error: ")
      print(e)

   finally:
      connection.close()



   ### Step:3 Show output in Monitor------------
   message = str(t) +"C"
   print(message)


   ### Step:4 Show output in Sensehat LEDs------------
   # sense.show_message(message, text_colour = white, back_colour = black, scroll_speed = 0.1)


   ### Step:5 Wait 2 seconds and repeat------------
   time.sleep(2)

   ### For Testing: Stopping infiniteloop after one execution------------
   break
