# -*- coding: utf-8 -*-

import cv2
import numpy as np
from glob import glob
import json


def main():
    # ファイル名宣言
    imreadName = "mov0.jpg"              # 読み込む画像ファイル名
    imwriteName = "image_correction.jpg"    # 歪み補正済み画像ファイル名
    jsonName = "calibrateParameter.json"    # 読み込むJSONファイル名
    
    # パターン宣言
    square_size = 23.0      # パターン1マスの1辺サイズ[mm]
    pattern_size = (10, 7)  # パターンの行列数
    
    # Object Points(ワールド座標系), Image Points(画像座標系)宣言
    pattern_points = np.zeros((np.prod(pattern_size), 3), np.float32)
    pattern_points[:, :2] = np.indices(pattern_size).T.reshape(-1, 2)
    pattern_points *= square_size
    object_points = []      # 3D point in real world spece
    image_points = []       # 2D point in image plane
    
    # termination criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    
    # 内部パラメータの読み込み
    inputfile = open(jsonName, "r")
    data = json.load(inputfile)
    inputfile.close()
    
    cameraMatrix = np.array(data["CameraMatrix"])
    distCoeffs =np.array(data["DistortCoeffs"])
     
    # 画像の取得
    image = cv2.imread(imreadName, 0)
    # チェスボードのコーナーを検出
    found, corners = cv2.findChessboardCorners(image, pattern_size)
    # コーナーを検出した場合
    if found:
        print "Success : chessboard found"
        cv2.cornerSubPix(image, corners, (11, 11), (-1, -1), criteria)
    # コーナを検出できない場合
    if not found:
        print "Fail : chessboard not found"
        return
    image_points.append(corners.reshape(-1, 2))
    object_points.append(pattern_points)
    imagePoints = np.array(image_points)
    objectPoints = np.array(object_points)
    
    # solvePnP
    retval, rvec, tvec = cv2.solvePnP(objectPoints, imagePoints, cameraMatrix, distCoeffs)
    print "retval: ", retval
    print "rvec: ", rvec
    print "tvec:", tvec
    
    # 歪み補正
    newcamera, roi = cv2.getOptimalNewCameraMatrix(cameraMatrix, distCoeffs, image.shape, 0)
    image_correction = cv2.undistort(image, cameraMatrix, distCoeffs, None, newcamera)
    
    # 補正した画像の保存
    cv2.imwrite(imwriteName, image_correction)


if __name__ == '__main__':
    main()
