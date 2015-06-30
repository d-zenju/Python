# -*- coding: utf-8 -*-


import cv2
import numpy as np


windowName = 'image'
cv2.namedWindow(windowName)

def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)


def main():
    img = cv2.imread('ship.jpg')
    cv2.setMouseCallback(windowName, on_mouse)

    while(1):
        cv2.imshow(windowName, img)
        if cv2.waitKey(33) & 0xFF == 27: break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
