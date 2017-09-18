#!/usr/bin/env python3
# To use, either
#  1. name any of the advertfiles `advertfile` and run advert.py without additional arguments
#  2. pass the name of the advertfile you want to use as the first additional argument to advert.py

import sys, random

advertfile = sys.argv[1] if len(sys.argv) > 1 else 'advertfile'

ads = []

with open(advertfile, 'r') as f:
    ads = f.read().split('\n%\n')

while True:
    try:
        ads.remove('')
    except:
        break

print('Advertisement:', random.choice(ads))
