# Write a Python function which display timer(in Seconds)

import time  

def timer(i):
    
    while i>0:
        print(i)
        time.sleep(1)
        i-= 1


try:
    i = int(input('Set the Timer for (Seconds): '))
    int(i)
    timer(i)
except ValueError:
    print('Input is not an INTEGER !')
