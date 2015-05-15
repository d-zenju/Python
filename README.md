python
======

# calibration
キャリブレーションに関するコード

## calibration.py
ディレクトリ内にあるすべてのグレースケール画像をキャリブレーションする
キャリブレーション結果はJSONで出力される

## distortionCorrection.py
キャリブレーション結果(JSON)から画像を1枚, 歪み補正する
なお、コマンドに出力される結果のtvecのZ座標は、パターンまでの距離を示す

## cameraCapture.py
接続されているカメラを表示し、キャプチャーする
キャプチャーする場合はSpaceキー, 終了はESCキーとなっている

## videoCapture.py
動画ファイルを表示し、キャプチャーする
キャプチャーする場合はSpaceキー, 終了する場合はESCキーとなっている

# calcurate.py
カメラパラメータと画像から距離を算出する

# mouse.py
左クリックを押すと、座標が表示される

# realvideo.py
webカメラをリアルタイムに表示する

===
# LICENSE
This software is released under the MIT License, see [LICENSE.txt](https://github.com/d-zenju/python/blob/master/LICENSE.txt "LICENSE.txt").
