## EXAMPLE CODE
# Set a GPIO to output, and alternate the output between LOW and HIGH every 5 seconds

import time
import onionGpio

gpioNum = 1
gpioObj	= onionGpio.OnionGpio(gpioNum)

# set to output 
status 	= gpioObj.setOutputDirection(0)		# initialize the GPIO to 0 (LOW)

# alternate the value
value 	= 0
while True:
	# reverse the value
	if value == 0:
		value = 1
	else:
		value = 0
	
	# set the new value
	status 	= gpioObj.setValue(value)
	print('GPIO{} set to: {}'.format(gpioNum, value))
	
	time.sleep(5)

