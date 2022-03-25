import pyautogui
import os
import time;


print("Tell me should I move in : ")
def option():
    print("Minutes - 1")
    print("Seconds - 2")
    n = input()
    if(n == '1'):
        print("How many minutes?")
        timetable = input()
        mouseMove(n,timetable) 
    if(n == '2'):
        print("How many seconds?")
        timetable = input()
        mouseMove(n,timetable) 
    else:
        os.system('cls')
        print("Select a valid option")
        option()

def mouseMove(n,timetable):
    print('Press Ctrl + C to quit.')
    if(n == '1'):
        while(True):
            time.sleep(int(timetable)*60) #convert to minutes
            pyautogui.move(0, 2)
    else:
        while(True):
            time.sleep(int(timetable))
            pyautogui.move(0, 2)

option()