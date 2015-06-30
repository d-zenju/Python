# -*- coding: utf-8 -*-

import cv2
import numpy as np


def main():
    bg = cv2.imread("../mv001bg.png", 0)  # background
    im = cv2.imread("../mv001.png", 0)   # image
    (w, h) = (im.shape[0], im.shape[1])
    mask = np.zeros((w, h), np.uint8)
    diff = cv2.absdiff(im, bg)
    fg = diff > 10
    mask[fg] = 255
    
#    k = np.ones((5, 5), np.uint8)
#    mask = cv2.dilate(mask, k, 2)
#    mask = cv2.erode(mask, k, 2)
    mask = cv2.medianBlur(mask, 7)
        
    obj = cv2.bitwise_and(im, mask)

    cv2.imwrite("mask.png", mask)
    
    cv2.imshow("mask", mask)
    cv2.imshow("object", obj)
    cv2.waitKey(0)
    cv2.deftroyAllWindows()


if __name__ == "__main__":
    main()
