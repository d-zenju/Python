# -*- coding: utf-8 -*-

import cv2

 
def main():
    # ファイル名(接頭語設定)
    headName = "test"
    
    # カメラ映像の取得
    capture = cv2.VideoCapture(0)
    i = 0
    while True:
        ret, image = capture.read()
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Camera capture",image_gray)
        # スペースキーが押されたら画像を保存
        if cv2.waitKey(33) == 32:
            cv2.imwrite(headName + str(i)+ ".jpg", image_gray)
            print("Save image : "+ headName + str(i) + ".jpg")
            i += 1
        # Escキーが押されたら終了
        elif cv2.waitKey(33) == 27:
            capture.release()
            cv2.destroyAllWindows()
            break
 

if __name__ == '__main__':
    main()
