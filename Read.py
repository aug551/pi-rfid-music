#!/usr/bin/env python

import subprocess
import os
import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from os import walk

reader = SimpleMFRC522()
path = (os.path.dirname(os.path.realpath(__file__)) + '/music/')

existFlag = False

while True:
    try:
        print('Place tag to read...')
        id, text = reader.read()

        if os.path.exists(str.rstrip(path + text)):
            print('true')
            songs = next(walk(str.rstrip(path + text)), (None, None, []))[2]
            songs.sort()
            for song in songs:
                # toPlay = path + str.rstrip(text) + '/\'' + song + '\''
                toPlay = path + str.rstrip(text) + '/' + song

                # os.system("ffplay -nodisp -autoexit " + toPlay)
                process = subprocess.Popen(['ffplay', '-nodisp', '-autoexit', toPlay], stdout=subprocess.PIPE)
                textP = process.communicate()[0]
                print('Running in: ', process.pid)
                # print(process.poll())
                while process.poll() is None:
                    time.sleep(0.25)
                print(path + str.rstrip(text) + '/\'' + song)

                print('\n\n\nStarting next song...')
    except KeyboardInterrupt:
        print(textP)
        GPIO.cleanup()
        break
    finally:
        time.sleep(2)

