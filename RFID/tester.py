from time import sleep
from mfrc522 import SimpleMFRC522
import socket
import RPi.GPIO as GPIO
reader = SimpleMFRC522()

RECEIVER_IP = "10.0.100.146"  
PORT = 6767

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # Loopar tills användaren gör ctrl + c
    while True:
        print("Hold a tag near the reader")
        id, text = reader.read() # Väntar tills en tagg / kort läses
        print(f"ID: {id}")
        print(f"Text: {text}")
        sock.sendto(str(id).encode("utf-8"), (RECEIVER_IP, PORT))
        sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()
    exit()
