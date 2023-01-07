#!/usr/bin/env python3
'''
Python 6 nodarbības mājasdarbs Nr.3

Uzdevums: aizpildīt vietas ar atzīmi TODO
'''

import numpy as np
import cv2

# importēt "python.jpg" bildi
img = cv2.imread("python.jpg")
print(img.shape)
cv2.imshow('image', img)
cv2.waitKey(0)

# Pārveidot bildi melnbaltu un izvadīt uz ekrāna
img_melnbalts = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('image', img_melnbalts)
cv2.waitKey(0)

# pielietot Caddy edge detection uz originālās bildes un izvadīt uz ekrāna
img_caddy = cv2.Canny(img, 10, 200)
cv2.imshow('image', img_caddy)
cv2.waitKey(0)

# Pārveidot TIKAI zilo krāsu par sarkanu un izvadīt uz ekrāna
img_zils_sarkans = img.copy()
hsv = cv2.cvtColor(img_zils_sarkans, cv2.COLOR_BGR2HSV)
lower_range = np.array([110,50,50])
upper_range = np.array([130,255,255])
mask = cv2.inRange(hsv, lower_range, upper_range)
img_zils_sarkans[mask != 0] = [0,0,255]
cv2.imshow('image', img_zils_sarkans)
cv2.waitKey(0)

cv2.destroyAllWindows()