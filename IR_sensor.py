# import the necessary library
import RPi.GPIO as IO

# setting warning to false , make our robot don't receive warnings during runtime
IO.setwarnings(False)

# setting this mode to refer the pins by their function number
IO.setmode(IO.BCM)

# setting the appropriate pins to IR sensors
IO.setup(2,IO.IN) #GPIO 2 -> Left IR out
IO.setup(3,IO.IN) #GPIO 3 -> Right IR out
IO.setup(5,IO.IN) #GPIO 5 -> center IR out

# setting the appropriate pins to the motors 
IO.setup(4,IO.OUT) #GPIO 4 -> Motor 1 terminal A
IO.setup(14,IO.OUT) #GPIO 14 -> Motor 1 terminal B

IO.setup(17,IO.OUT) #GPIO 17 -> Motor Left terminal A
IO.setup(18,IO.OUT) #GPIO 18 -> Motor Left terminal B


while 1:

    #Left and right are white and center is black : we move forward  
    #Left and right and center are white : we move forward 
    if(IO.input(2)==True and IO.input(3)==True) :  

        IO.output(4,True) #1A+
        IO.output(14,False) #1B-

        IO.output(17,True) #2A+
        IO.output(18,False) #2B-

    #Left is black and right is white : we turn right
    elif(IO.input(2)==False and IO.input(3)==True): #turn right  
        
        IO.output(4,True) #1A+
        IO.output(14,True) #1B-

        IO.output(17,True) #2A+
        IO.output(18,False) #2B-

    #Left is black and right is white : we turn left
    elif(IO.input(2)==True and IO.input(3)==False): 

        IO.output(4,True) #1A+
        IO.output(14,False) #1B-

        IO.output(17,True) #2A+
        IO.output(18,True) #2B-

    #Left and right and center are black : we stop
    elif(IO.input(2)==False and IO.input(3)==False and IO.input(5)==False): 

        IO.output(4,True) #1A+
        IO.output(14,True) #1B-

        IO.output(17,True) #2A+
        IO.output(18,True) #2B-