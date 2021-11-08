'''PYTHON PASSWORD GENERATOR'''

import random
lowerChar="abcdefghijklmnopqrstuvwxyz"
upperChar="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="[]{}()*;/,-_"

mixAll= lowerChar + upperChar + numbers + symbols

lenth = 16
password= "".join(random.sample(mixAll,lenth))
print(password)