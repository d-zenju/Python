#-*- coding: utf-8 -*-

import cv2


windowName = "drawSample"
cv2.namedWindow(windowName)
img = cv2.imread("sample.png")
point = [-1, -1]


def mouse(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        point[0] = x
        point[1] = y       


def main():
    while(1):
        cv2.imshow(windowName, img)
        cv2.setMouseCallback(windowName, mouse)
        cv2.line(img, (0, point[1]), (200, point[1]), (0, 0, 255), 2)
        
        if cv2.waitKey(33) & 0xFF == 27: break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
