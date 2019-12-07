import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    c=n%2
    if c>0:
        print('Weird')
        #print(n)
    if c==0:
        if n in range(2,6):
            #print(n)
            print('Not Weird')
        if n in range(6,21):
            #print(n)
            print('Weird')
        if n>20:
            print('Not Weird')
