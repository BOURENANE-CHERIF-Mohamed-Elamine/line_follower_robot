#!/usr/bin/env python
# coding: utf-8

# In[1]:


# this is the main program to connect the parts, still in progress

import RPI.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
SDA=17
SCL=27
led=26

m1a=23
m1b=24
m2a=25
m2b=8

GPIO(SDA,GPIO.OUT)
GPIO(SCL,GPIO.IN)
GPIO(led,GPIO.OUT)

GPIO(ma1,GPIO.OUT)
GPIO(m1b,GPIO.OUT)
GPIO(m2a,GPIO.OUT)
GPIO(m2b,GPIO.OUT)
time.sleep(5)

def stop():
    GPIO.output(m1a, 0)
    GPIO.output(m1b, 0)
    GPIO.output(m2a, 0)
    GPIO.output(m2b, 0)
    
def forward():
    GPIO.output(m1a, 1)
    GPIO.output(m1b, 0)
    GPIO.output(m2a, 1)
    GPIO.output(m2b, 0)
    
def left():
    GPIO.output(m1a, 1)
    GPIO.output(m1b, 0)
    GPIO.output(m2a, 0)
    GPIO.output(m2b, 0)

stop()

while True:
    GPIO.output(SDA, 0)
    time.sleep(0.1)
    GPIO.output(SDA, 1)
    time.sleep(0.00001)
    GPIO.output(SDA, 0)
    
    # check SCL LOW
    while GPIO.input(SCL)==0:
        GPIO.output(led, False)
    pulse_start = time.time()
    
    # check SCL LOW
    while GPIO.input(SCL)==1:
        GPIO.output(led, True)
        
    pulse_start = time.time()
    pulse_duration = pulse_end- pulse_start
    distance= pulse_duration*17150
    distance= round(distance, 2)
    print(distance)
    
    # check distance less then 2cm
    
    if distance < 2:
        left()
        time.sleep(1)
    else:
        forward()
        
    
    
    


# In[ ]:




