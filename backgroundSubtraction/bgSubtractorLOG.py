# -*- coding: utf-8 -*-
import numpy as np
import cv2

cap = cv2.VideoCapture("../mv001.mov")
fgbg = cv2.imread("../mv001bg.png")
bggray = cv2.cvtColor(fgbg, cv2.COLOR_BGR2GRAY)

count = 0

while(1):
    ret, frame = cap.read()    
    
    imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    (w, h) = (imgray.shape[0], imgray.shape[1])
    fgmask = np.zeros((w, h), np.uint8)
    
    diff = cv2.absdiff(imgray, bggray)
    fg = diff > 30
    fgmask[fg] = 255
    
    #frame = imgray.apply(fgmask)
    #frame = cv2.medianBlur(fgmask, 7)
    
    # cv2.imshow('frame',frame)
    # cv2.imshow('mask', fgmask)
    
    cv2.imshow("img", imgray)
    #cv2.imshow("bg", bggray)
    cv2.imshow("mask", fgmask)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
