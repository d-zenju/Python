# -*- coding: utf-8 -*-
import cv2
import numpy as np
 
 
if __name__ == '__main__':
 
    # 入力画像の取得
    im_in = cv2.imread("mask.png")
    # グレースケール変換
    im_gray = cv2.cvtColor(im_in,cv2.COLOR_BGR2GRAY)
    # 2値化
    ret,thresh = cv2.threshold(im_gray,127,255,0)
    # 角検出
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    print len(contours)
    cnt=contours[1]
 
    # 凸包を描く
    hull = cv2.convexHull(cnt)
    cv2.drawContours(im_in,[hull],0,(255,0,0),2)
 
    # 矩形を描く
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(im_in,(x,y),(x+w,y+h),(0,255,0),1)
 
    # 輪郭を描く
    cv2.drawContours(im_in,contours,0,(0,0,255),2)
 
    # 画像表示
    cv2.imshow("Edge Image",im_in)
    # キー入力待機
    cv2.waitKey(0)
    # ウィンドウ破棄
    cv2.destroyAllWindows()
