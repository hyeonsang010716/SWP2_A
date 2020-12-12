import random
from getWeatherData import *
temp = int(getTemp())
#temp = int(input("Enter today's temperature: "))

cl = {}
cl = {'outer':['padding', 'coat', 'jacket', 'zipup'],
      'top_l':['tee', 'mtm', 'hood', 'shirt', 'knit'],
      'top_s':['tee', 'shirt'],
      'pants':['long', 'short'],
      'skirt':['long', 'short']
      }
# cl = {'outer': {'padding':[], 'coat':[], 'jacket':[], 'zipup':[]},
#       'top_l': {'tee':[], 'mtm':[], 'hood':[], 'shirt':[], 'knit':[]},
#       'top_s': {'tee':[], 'shirt':[]},
#       'pants': {'long':[], 'short':[]},
#       'skirt': {'long':[], 'short':[]}
#       }

r_num0 = random. randint(0,2)
r_num1 = random.randint(3,4)
r_num2 = random.randint(0,len(cl['top_l'])-1)
r_num3 = random.randint(0,len(cl['top_s'])-1)

if temp < 5:
    print(cl['outer'][0], cl['top_l'][r_num0], cl['pants'][0])
    print(cl['outer'][1], cl['top_l'][r_num1], cl['pants'][0])

if 6 <= temp < 17:
    print(cl['outer'][2], cl['top_l'][r_num1], cl['pants'][0])
    print(cl['outer'][3], cl['top_l'][r_num0], cl['pants'][0])

if 17 <= temp < 24:
    print(cl['top_l'][r_num2], cl['pants'][0])

if 24 <= temp < 28:
    print(cl['top_s'][r_num3], cl['pants'][0])

if temp >= 28:
    print(cl['top_s'][r_num3], cl['pants'][1])