import time
import random
kerdez = int(input("Hányszór szeretnél dobni? ="))
for i in range (kerdez):
    x = random.randint(1,6)
    print (x)
    time.sleep(2)
if x == 1:
    print('   o  o  o ')
    print('   o  @  o ')
    print('   o  o  o ')
elif x == 2:
    print('   o  o  o ')
    print('   @  o  @ ')
    print('   o  o  o ')
elif x == 3:
    print('   o  o  @ ')
    print('   o  @  o ')
    print('   @  o  o ')
elif x == 4:
    print('   @  o  @ ')
    print('   o  o  o ')
    print('   @  o  @ ')
elif x == 5:
    print('   @  o  @ ')
    print('   o  @  o ')
    print('   @  o  @ ')
elif x == 6:
    print('   @  o  @ ')
    print('   @  o  @ ')
    print('   @  o  @ ')