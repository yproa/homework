# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 14:45:23 2021

@author: hariz
"""

from mss import mss
import pyautogui
import time
import cv2
import numpy as np

def monitor_part(img): 
    x_dino = 740
    y_dino = 280
    box_width = 140#200      
    box_height = 25#15
    cactus = img[y_dino:y_dino+box_height, x_dino:x_dino + box_width]
    
    return cactus
         
sreen_tool = mss()   
x, y = pyautogui.position()

replayBtn=(948,348)#695   

pyautogui.click(replayBtn)
pyautogui.keyDown('space')
                    
count=0
while x< 1920:
    img = cv2.imread(sreen_tool.shot())
    cactus = monitor_part(img)
    cactus_gray = cv2.cvtColor(cactus, cv2.COLOR_BGR2HSV)
    ready_cactus = cv2.inRange(cactus_gray, np.array([0, 0, 0]), np.array([255, 255, 100]))  
    conts, hier = cv2.findContours(ready_cactus, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(conts)>0:
        pyautogui.keyDown('space')
        time.sleep(0.04)
        pyautogui.keyUp('space')
        count+=1
        print("jump ", count)
             
    x, y = pyautogui.position()      