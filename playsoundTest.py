#!/usr/bin/env python

from cgitb import text
from concurrent.futures import thread
import threading
import time
from tracemalloc import stop

start = time.perf_counter()
stopFlag = False

def loop():
    while True:
        time.sleep(0.15)
        if stopFlag:
            print('done looping')
            break

t1 = threading.Thread(target=loop)

t1.start()

while True:
    text = input('Command: ')
    if text == 'stop':
        stopFlag = True
        break


t1.join()


finish = time.perf_counter()

print(f'Loop excecuted in {round(finish-start, 2)} second(s)')