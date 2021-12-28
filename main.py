import pyautogui,time
time.sleep(5)
beemovie = open("beemovie.txt", 'r')
for word in beemovie:
    pyautogui.typewrite(word)

