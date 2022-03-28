from turtle import position
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
        timetable = int(input())
        mouseMove(n,timetable)
    elif(n == '2'):
        print("How many seconds?")
        timetable = int(input())
        mouseMove(n,timetable) 
    else:
        os.system('cls')
        print("Select a valid option")
        option()

def mouseMove(n,timetable):
    print('Press Ctrl + C to quit.')
    if(n == '1'):
        timetable = timetable*60
    while(True):
        pyautogui.move(0, 1)
        time.sleep(timetable) #convert to minutes
        pyautogui.move(0, -1)

option()