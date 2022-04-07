#!/usr/bin/env Python
# -*- codingL utf-8 -*-
"""
@author: sandyzikun
@title: Computing Pi
"""
import random, math, time
class Constants(object):
    DARTS = 2 ** 11 #int(1E+04)
hits = 0.
time.process_time()
for k in range(Constants.DARTS):
    x, y = random.random(), random.random()
    if math.sqrt(x ** 2 + y ** 2) <= 1.:
        hits += 1.
pi = 4 * (hits / Constants.DARTS)
print("Pi=%s" % pi)
print("Time of Processing: {:5.5}s".format(time.process_time()))