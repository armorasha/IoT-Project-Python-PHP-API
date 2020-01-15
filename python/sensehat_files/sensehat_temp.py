from sense_hat import SenseHat

sense = SenseHat()
##sense.set_rotation(180)
sense.clear()

blue = (0,0,255)
yellow = (255,255,0)
red = (255,0,0)
black = (0,0,0)
grey = (55,55,55)
white = (255,255,255)



while True:
   temp = sense.get_temperature()
   t= round(temp,1)
   message = str(t) +"C"
   print(message)
   sense.show_message(message, text_colour = white, back_colour = black, scroll_speed = 0.1)
