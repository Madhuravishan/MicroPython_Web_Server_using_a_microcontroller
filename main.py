from machine import Pin
from time import sleep
import dht 

 ######################### Change Following Code ################################

# Define Which pin you are connecting dht data pin (In here use 14)
DHT_PIN = 2

# Create a pin object 

# Pass above created pin object to DHT11 Library 
# You may use following when needed
# sensor = dht.DHT22(pin)

################################################################################


while True:
  try:
    sleep(2)
    
 ######################### Change Following Code ################################


    # Use measure method to read from DHT11  
    # There is a method for reading from dht11 called measure()
    
    # Read Tempurature from the dht11
    # There is method to read tempurature tempurature()
    
    # Read Humidity from the dht11
    # There is method to read tempurature tempurature()

    # Print Tempurature and Humidity 

################################################################################
######################### Do Not Change Following Code #########################

  except OSError as e:
    print('Failed to read sensor.')