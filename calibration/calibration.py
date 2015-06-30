# -*- coding: utf-8 -*-

import cv2
import numpy as np
from glob import glob
import json


def main():
    # ファイル名宣言
    jsonName = "calibrateParameter.json"
    
    # パターン宣言
    square_size = 23.0      # パターン1マスの1辺サイズ[mm]
    pattern_size = (10, 7)  # パターンの行列数
    # prepare object points
    pattern_points = np.zeros((np.prod(pattern_size), 3), np.float32)
    pattern_points[:, :2] = np.indices(pattern_size).T.reshape(-1, 2)
    pattern_points *= square_size
    object_points = []      # 3D point in real world spece
    image_points = []       # 2D point in image plane
    # termination criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    apertureWidth = 0       # 物理センサの幅[mm]
    apertureHeight = 0      # 物理センサの高さ[mm]
    
    for filename in glob("*.jpg"):
        # 画像の取得
        image = cv2.imread(filename, 0)
        print "loading : " + filename
        # チェスボードのコーナーを検出
        found, corners = cv2.findChessboardCorners(image, pattern_size)
        # コーナーを検出した場合
        if found:
            print "Success : chessboard found"
            cv2.cornerSubPix(image, corners, (11, 11), (-1, -1), criteria)
        # コーナを検出できない場合
        if not found:
            print "Fail : chessboard not found"
            continue
        image_points.append(corners.reshape(-1, 2))
        object_points.append(pattern_points)

    # 内部パラメータ計算
    retval, cameraMatrix, distCoeffs, rvecs, tvecs = cv2.calibrateCamera(object_points, image_points, image.shape[::-1])
    fovx, fovy, focalLength, principalPoint, aspectRatio = cv2.calibrationMatrixValues(cameraMatrix, image.shape[::-1], apertureWidth, apertureHeight)
     
    # 計算結果を表示
    print "RMS = ", retval
    print "cameraMatrix = \n", cameraMatrix
    print "distCoeffs = ", distCoeffs
    print "fovx = ", fovx
    print "fovy = ", fovy
    print "focalLength = ", focalLength
    print "principalPoint = ", principalPoint
    print "aspectRatio = ", aspectRatio
    
    # JSONの作成
    jsonObject = {}
    dic_retval = {"retval": retval}
    dic_cameraMatrix = {"CameraMatrix": cameraMatrix.tolist()}
    dic_distCoeffs = {"DistortCoeffs": distCoeffs.tolist()}
    dic_fovx = {"fov_x": fovx}
    dic_fovy = {"fov_y": fovy}
    dic_focalLength = {"focal_Length": focalLength}
    dic_principalPoint = {"principal_Point": principalPoint}
    dic_aspectRatio = {"aspect_Ratio": aspectRatio}
    jsonObject.update(dic_retval)
    jsonObject.update(dic_cameraMatrix)
    jsonObject.update(dic_distCoeffs)
    jsonObject.update(dic_fovx)
    jsonObject.update(dic_fovy)
    jsonObject.update(dic_focalLength)
    jsonObject.update(dic_principalPoint)
    jsonObject.update(dic_aspectRatio)
    
    outfile = open(jsonName, "w")
    json.dump(jsonObject, outfile)
    outfile.close()


if __name__ == '__main__':
    main()
