#!/usr/bin/env python

import os
from os import walk
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

# get all songs from music folder


musicPath = (os.path.dirname(os.path.realpath(__file__)) + '/music')

if(os.path.exists(musicPath) == False):
    os.mkdir(musicPath)
    print('directoryCreated')

folders = os.listdir(musicPath)

if(len(folders) == 0):
    print('no music')
    
else:
    for i in range(len(folders)):
        print(str(i) + '. ' + folders[i] + '\n')

    try:
        music = input('Choose music to write(0 - %d): ' %(len(folders)-1))
        print('Place tag to write...')
        reader.write(folders[int(music)])
        print('Done.')
    except KeyboardInterrupt:
        GPIO.cleanup()
    finally:
        GPIO.cleanup()

