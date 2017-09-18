import random

ads = []

with open('advertfile', 'r') as f:
    ads = f.read().split('\n%\n')

while True:
    try:
        ads.remove('')
    except:
        break

print('Advertisement:', random.choice(ads))
