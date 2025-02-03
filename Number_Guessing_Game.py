#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chyas
#
# Created:     31/01/2025
# Copyright:   (c) chyas 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
Cnum = random.randrange(1,101)
print("-----Welcome To Number Guessing Game")

while True:
   Unum=int(input("Enter your Number"))
   if Cnum>Unum:
    print(f"Computer Number {Cnum}")
    print("Your Number is lower than Computer Number")

   elif Cnum<Unum:
    print(f"Computer Number {Cnum}")
    print("Your Number is Higher than Computer Number")

   else:
    print(f"Computer Number {Cnum}")
    print("Your Number is matched with Computer Number \n Hurrah! You won")
    break
