#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import time

reader = SimpleMFRC522.SimpleMFRC522()

try:
    print("First, writing to the tag...")
    text = input('Enter new data to write to tag, then hit Enter: ')
    print("Place your tag next to the antenna to write")
    reader.write(text)

    print("Wait 5 seconds...")
    time.sleep(5)

    print("Now, reading tag - place it next to the antenna...")
    id, text = reader.read()

finally:
    GPIO.cleanup()

