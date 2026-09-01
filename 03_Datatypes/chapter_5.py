# isme kya hota h ki jb hmare pass floating values jyda hoti h 
# to merko accurate values k lie system libnrary import krni hot h and uska use krke kr skta hu
#  system library PC k according vary kr skti h 
#  from module_name import class, function

import sys;
from sys import version
from decimal import Decimal
ideal_temp = 97.5
current_temp = 56.9999999999999

print(F"Ideal_temp is {ideal_temp}")
print(F"current_temp is {current_temp}")
print(F"Diffrence is {Decimal(ideal_temp - current_temp)}")
print(version)