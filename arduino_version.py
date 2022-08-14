#pip install adafruit-blinka
from pyfirmata import Arduino,util
import pyfirmata

import time
import Adafruit_TCS34725
import busio
import board
i2c = busio.I2C(board.SCL, board.SDA)
tcs = Adafruit_TCS34725.TCS34725(i2c)
tcs.set_interrupt(False)

find = False
i=1
while find==False:
    try:
        carte = Arduino("com"+str(i))
        acuisition = util.Iterator(carte)
        acuisition.start()
        find= True
    except:
        i += 1
"""
your code 
"""
#RED = 5
#GREEN = 6
#BLUE = 7


pr = carte.get_pin('d:5:o')
pg = carte.get_pin('d:6:o')
pb = carte.get_pin('d:7:o')

pr.start(255)
pg.start(255)
pb.start(255)

try:
    while True:
        r, g, b, c = tcs.get_raw_data()
        if((r > b) and (r >g)):
            if(b <5):
                #red
                #moteur.stop()
                pr.ChangeDutyCycle(80)
                pg.ChangeDutyCycle(1)
                pb.ChangeDutyCycle(1)



        elif((r < b) and (b >5)):
            #blue
            #moteur.stop()
            pr.ChangeDutyCycle(1)
            pg.ChangeDutyCycle(1)
            pb.ChangeDutyCycle(80)
            #time.sleep(2)
            #moteur.start()

        elif((r < g) and (b <g) and (g>20)):
            if (b<10):
                #green
                #moteur.stop()
                pr.ChangeDutyCycle(1)
                pg.ChangeDutyCycle(80)
                pb.ChangeDutyCycle(1)
                #time.sleep(5)
                #moteur.start()
        else:
            #default color black
            pr.ChangeDutyCycle(255)
            pg.ChangeDutyCycle(255)
            pb.ChangeDutyCycle(255)
except KeyboardInterrupt:
    pass


#Clean things up at the end

tcs.set_interrupt(True)
tcs.disable()
pr.stop()
pg.stop()
pb.stop()





carte.exit()
