# -*- coding: utf-8 -*-
"""
Created on Sun Dec 3 13:16:49 2018

@author: Alan Jerry Pan, CPA, CSc student
@affiliation: Shanghai Jiaotong University

program framework for object overflow

Suggested citation as computer software for reference:
Pan, Alan J. (2018). Overflow [Computer software]. Github repository <https://github.com/alanjpan/Overflow>

Note this software's license is GNU GPLv3.
"""

import math
import random

capacity = [100, 100, 100, 100, 100]
actual = [0, 0, 0, 0, 0]

def flow():
    select = random.randrange(0, 5, 1)
    pour = random.randrange(1, 20, 1)

    actual[select] = actual[select] + pour
    print('*pour ' + str(pour) + ' units into cup #' + str(select))
    overflow()

def overflow():
    for i in range(len(capacity)):
        if actual[i] > capacity[i]:
            print(actual)
            distribute = actual[i] - capacity[i]
            #flow into two possible directions: left or right
            actual[i] = 100
            flow = (distribute / 2)
            if i == 0:
                actual[1] = int(actual[1] + flow)
                print(str(flow) + ' units overflow over left edge')
            elif i == 4:
                actual[5] = int(actual[5] + flow)
                print(str(flow) + ' units overflow over right edge')
            else:
                actual[i-1] = int(actual[i-1] + flow)
                actual[i+1] = int(actual[i+1] + flow)
    for i in range(len(capacity)):
        if actual[i] > capacity[i]:
            overflow()

for i in range(40):
    flow()
print(actual)