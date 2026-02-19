from time import sleep
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
reader = SimpleMFRC522()

try:
    # Loopar tills användaren gör ctrl + c
    while True:
        print("Hold a tag near the reader")
        id, text = reader.read() # Väntar tills en tagg / kort läses
        print(f"ID: {id}")
        print(f"Text: {text}")
        sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()
    exit()
