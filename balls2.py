# -*- coding: utf-8 -*-

"""
Created on Mon Nov 16 18:17:22 2020

@author: Юрий
"""
import cv2
import numpy as np
from random import randint

def set_upper(x):
    global colorUpper
    colorUpper[0] = x
    
def set_lower(x):
    global colorLower
    colorLower[0] = x
    
def cntr(curr_x, curr_y):
    cv2.circle(frame, (int(curr_x), int(curr_y)), int(radii), (0,255,255), 2)
        
cam = cv2.VideoCapture(0)
cv2.namedWindow("Camera", cv2.WINDOW_KEEPRATIO)
cv2.namedWindow("Mask", cv2.WINDOW_KEEPRATIO)

cv2.createTrackbar("U", 'Mask', 0, 255, set_upper)
cv2.createTrackbar("L", 'Mask', 0, 255, set_lower)

colorLower = np.array([0,0,0], dtype = "uint8")
colorUpper = np.array([255,255,255], dtype = "uint8")

lowers=[56,25,100]#green yellow blue
uppers=[72,25,102]#green yellow blue
colors1=['green', 'yellow' ,'blue']
colors2=['green', 'yellow' ,'blue']
for qq in range(5):
    colors2.append(colors2.pop(randint(0,2)))
print("Расположите шарики в таком порядке:")
print(colors2)
balls={}
for qw in colors1:
    balls[qw]=-1
while cam.isOpened():
    for qq in range(3):
        set_lower(lowers[qq])
        set_upper(uppers[qq])
        ret, frame = cam.read()
        blurred = cv2.GaussianBlur(frame, (11,11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        
        mask = cv2.inRange(hsv, colorLower, colorUpper)
        mask = cv2.erode(mask, None, iterations = 2)
        mask = cv2.dilate(mask, None, iterations = 2)
        
        cnts, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(cnts) >0:
            c = max(cnts, key = cv2.contourArea)
            (curr_x, curr_y), radii = cv2.minEnclosingCircle(c)
            if radii > 10:
                balls[colors1[qq]]=curr_x
                cntr(curr_x, curr_y)
        
        cv2.imshow("Mask", mask)
        cv2.imshow("Camera", frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    # print(balls)
    if (balls[colors2[0]]==max(balls.values()))and(balls[colors2[2]]==min(balls.values())) and (min(balls.values())>0):
        print("You win!")
        break
    for qw in colors1:
        balls[qw]=-1
    
cam.release()
cv2.destroyAllWindows()    