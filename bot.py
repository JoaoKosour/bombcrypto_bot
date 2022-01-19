from pyautogui import locateOnScreen, moveTo, press, click, easeInOutQuad
from time import sleep
from random import seed, randint, random


seed(1)
print('MAKE SURE YOU ARE IN THE GAME WINDOWS WHEN YOU RUN THE PROGRAM')
numchar = input("Enter number of characters: ")


def check_status_error():
    if (locateOnScreen('ok.PNG') is not None):
        moveTo('ok.PNG', duration=(random()*3), tween=easeInOutQuad)
        sleep(randint(1, 3))
        click()
        solve_status_error()
    else:
        return
    if(locateOnScreen('enter_game.png') is not None):
        moveTo('enter_game.png', duration=(random()*3), tween=easeInOutQuad)
        sleep(randint(1, 3))
        click()
    else:
        sleep(randint(15, 23))
        press('f5')
        sleep(randint(60, 72))
        check_status_error()


def solve_status_error():
    move_click(950, 772)
    move_click(880, 615)
    sleep(10)
    moveTo('sign.PNG', duration=(random()*3), tween=easeInOutQuad)
    sleep(randint(1, 3))
    click()
    sleep(randint(25, 34))


def work():
    sleep(1)
    moveTo('return.png', duration=(random()*3), tween=easeInOutQuad)
    sleep(1)
    click()
    sleep(1)
    move_click(1350, 800)

    for x in range(5):
        move_click(850, (467+70*x))

    for x in range(11):
        scroll(-1000)

    for x in range(2):
        move_click(850, (700+70*x))

    moveTo(1000, 380)
    moveTo(950, 550)


def rest():
    sleep(1)
    moveTo('return.png', duration=(random()*3), tween=easeInOutQuad)
    sleep(1)
    click()
    sleep(1)
    move_click(1350, 800)
    for x in range(numchar):
        move_click(915, 467)
    move_click(1000, 380)
    move_click(950, 550)


def main():
    while(1):
        check_status_error()
        sleep(32 + randint(0, 27))
        rest()
        sleep(32 + randint(0, 27))
        check_status_error()
        sleep(7000 + randint(0, 500))
        check_status_error()
        sleep(32 + randint(0, 27))
        work()
        sleep(180 + randint(0, 27))


def move_click(pos1, pos2):
    moveTo(pos1 + randint(0, 10), pos2 + randint(0, 10),
           duration=(random()*3), tween=easeInOutQuad)
    sleep((random()*3))
    click()
    sleep((random()*5))


main()
