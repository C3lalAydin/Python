import pyautogui as pya
import time

time.sleep(5)


for x in range(0,20
):
    pya.typewrite(str(x), interval=0.001)
    pya.keyDown("shiftright")
    pya.press("enter")
    pya.keyUp("shiftright")
pya.press("enter")
