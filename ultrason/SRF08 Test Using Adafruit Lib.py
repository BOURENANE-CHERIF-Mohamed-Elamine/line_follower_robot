from pyfirmata import Arduino,util
import pyfirmata
import time
import Adafruit_GPIO.I2C as bus


carte = Arduino("com7")
acquisition = util.Iterator(carte)
acquisition.start()


i2c = bus.Device(0x70, 2)

bus.write16(i2c, 0x02, 0xff)

while True :

	bus.write16(i2c, 0x00, 0x51)
	time.sleep(0.1)
	print (bus.readS16(i2c, 0x03)+ '   ' + bus.readS16(i2c, 0x05))	
