import pyautogui




while(1):
    w = pyautogui.position()
    x_mouse = w.x
    y_mouse = w.y
    print(x_mouse, y_mouse)