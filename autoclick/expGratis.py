import keyboard as kb
import time as tm
import pyautogui as pg


def progr():
    flag=True
    while flag:
        tm.sleep(0.02)
        pg.leftClick()
        tm.sleep(0.01)
        pg.leftClick()
        pg.keyDown("ctrl")
        tm.sleep(0.01)
        pg.leftClick()
        tm.sleep(0.01)
        pg.leftClick()
        pg.keyUp("ctrl")
        flag=not kb.is_pressed("o")
    

def main():
    while True:
        if kb.is_pressed("p"):
            progr()
            break

if __name__=="__main__":
    main()

