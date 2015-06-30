# -*- coding: utf-8 -*-

import math


# camera
f = 0.00708481537
height = 23.0


# カメラキャリブレーション必須
py = 0.0156 / 3264.0
px = 0.0235 / 4912.0

# horizon
horizon = 617

# ship
shipx = 1479
shipy = 624

# image
imgh = 1080
imgw = 1920

# center考慮
hx = math.fabs(imgh / 2.0 - horizon)
sx = math.fabs(imgh / 2.0 - shipy)
sy = math.fabs(imgw / 2.0 - shipx)

print(hx, sx, sy)

theta = math.atan2(hx * py, f)
b = math.atan2(sy * py, f)
a = theta - b
z = height / math.tan(a)
x = px * sx * z / f
distance = math.sqrt(z * z + x * x)

print(distance)
