#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
from Adafruit_I2C import Adafruit_I2C as bus
i2c = bus(0x70)

bus.write16(i2c, 0x02, 0xff)

while True :

	bus.write16(i2c, 0x00, 0x51)
	time.sleep(0.1)
	print bus.readS16(i2c, 0x03), '   ' , bus.readS16(i2c, 0x05)	


# In[2]:





# In[3]:



        
        


# In[ ]:
