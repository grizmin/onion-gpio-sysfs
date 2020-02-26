from __future__ import print_function

import onionGpio

# Python2 compatibility
try:
    input = raw_input
except NameError:
    pass

# code is left 'as is' in order to be more readable for non-developers.

pin = 14

print('> Instantiating gpio object', end="")
gpio14 	= onionGpio.OnionGpio(pin)
print()

print('> Set direction to input... ', end="")
ret 	= gpio14.setInputDirection()
print('    returned {}'.format(ret))

print('> Get direction: ', end="")
direction 	= gpio14.getDirection()
print(direction)

print('> Read value: ', end="")
val		= gpio14.getValue()
print(val)



input('Ready to test output?')

print('> Set direction to output... ', end="")
ret 	= gpio14.setOutputDirection()
print('    returned {}'.format(ret))

print('> Get direction: ', end="")
direction 	= gpio14.getDirection()
print(direction)


print('> Read value: ', end="")
val		= gpio14.getValue()
print(val)


print('> Set value to 1... ', end="")
ret		= gpio14.setValue(1)
print('    returned {}'.format(ret))

print('> Read value: ', end="")
val		= gpio14.getValue()
print(val)

print()
print('> Set value to 0... ', end="")
ret		= gpio14.setValue(1)
print('    returned {}'.format(ret))

print('> Read value: ', end="")
val		= gpio14.getValue()
print(val)

print()
print('> Done!')
