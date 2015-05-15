# -*- coding: utf-8 -*-

import cv2


def main():
    # 動画ファイル名
    videoName = "BDMV.mov"
    
    # 画像ファイル名(接頭語)
    headName = "mov"
    
    # 動画取得
    src = cv2.VideoCapture(videoName)
    
    if not src.isOpened():
        print "Error: Can't open a video file"
        return
    
    # キー入力待機時間計算
    fps = (src.get(cv2.cv.CV_CAP_PROP_FPS))
    wait = (int)(1.0 / fps * 1000.0)        # キー入力待機時間[ms]
    
    i = 0
    
    # 動画再生(1フレームごと)
    while True:
        retval, frame = src.read()          # 1フレーム取得
        
        if frame is None:
            break
        
        cv2.imshow("video capture", frame)  # 1フレーム表示
        
        if cv2.waitKey(wait) == 32:         # キー入力待機, Spaceで保存(グレースケール)
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(headName + str(i) + ".jpg", image)
            print("Save image: " + headName + str(i) + ".jpg")
            i += 1
        elif cv2.waitKey(wait) == 27:       # キー入力待機, ESCで終了
            break
    
    cv2.destroyAllWindows()                 # すべての表示ウィンドウ破棄
    src.release()                           # ビデオファイルを閉じる


if __name__ == '__main__':
    main()
