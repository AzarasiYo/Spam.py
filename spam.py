print("作った人| https://youtu.be/qKQzT1Rehm8")

from pynput.keyboard import Key, Controller
import time

message = "こんちゃあ"
keyboard = Controller ()

time.sleep(3)

for num in range(3):
    for letter in message:
        keyboard.press(letter)
        keyboard.release(letter)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
