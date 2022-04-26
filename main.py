import os
import pyautogui
import pygetwindow as gw
import time

songName = "Doi saci de gunoi"
nrOfSessions = 1

f = open("accounts.txt", "r")
r = open("passW.txt", "r")
pyautogui.PAUSE = 0.8
stringMod = 'cmd /c "firefox -P "user1" -no-remote -new-instance"'

for i in range(nrOfSessions):
    stringMod = stringMod.replace(str(i), str(i+1))
    time.sleep(0.2)
    os.system(stringMod)

while True:
    lista = gw.getWindowsWithTitle('Mozilla Firefox')
    time.sleep(0.2)
    if len(lista) == nrOfSessions:
        break

print(gw.getWindowsWithTitle('Mozilla Firefox'))

windowsArr = gw.getWindowsWithTitle('Firefox')

for i in range(nrOfSessions):
    time.sleep(0.2)
    windowsArr[i].maximize()

for i in range(nrOfSessions):
    time.sleep(0.2)
    windowsArr[i].activate()

    # log in
    pyautogui.moveTo(960, 50)
    pyautogui.click()
    pyautogui.typewrite("https://accounts.spotify.com/en/login\n")
    time.sleep(4)
    pyautogui.moveTo(960, 480)
    pyautogui.click()
    pyautogui.typewrite(f.readline())
    pyautogui.moveTo(960, 550)
    pyautogui.click()
    pyautogui.typewrite(r.readline() + '\n')
    time.sleep(4)
    pyautogui.moveTo(960, 50)
    pyautogui.click()
    pyautogui.typewrite("https://open.spotify.com\n")
    time.sleep(4)

    # diamond hands
    pyautogui.moveTo(100, 220)
    pyautogui.click()
    time.sleep(4)
    pyautogui.typewrite(songName + '\n')
    time.sleep(4)
    pyautogui.moveTo(450, 300)
    pyautogui.click()
    pyautogui.moveTo(1815, 1035)
    pyautogui.click()
    pyautogui.moveTo(1055, 1035)
    pyautogui.click()
    pyautogui.click()
    time.sleep(2)
    windowsArr[i].minimize()

r.close()
f.close()
print("\nDone, all clients logged in and playing.")
