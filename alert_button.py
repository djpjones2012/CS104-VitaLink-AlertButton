from machine import Pin
import time
import requests

button = Pin(28, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        response = requests.post("https://api.telegram.org/bot8961798425:AAHvEZAgX3Mwa_y683SkrbLzsmrEuN_whVc/sendMessage", json = {"chat_id": "8850397136", "text":"Someone pressed the alert button!"})
        print("1",end=" ")
    else:
        print("0",end=" ")
    time.sleep(0.1)
