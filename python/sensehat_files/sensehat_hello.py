from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)

blue = (0,0,255)
yellow = (255,255,0)
red = (255,0,0)
black = (0,0,0)
grey = (55,55,55)
white = (255,255,255)

print("Hello World")
while True:
   sense.show_message("Hello World", text_colour = red, back_colour = grey, scroll_speed = 0.1)


print("Hello")
