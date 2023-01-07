#!/usr/bin/env python3
'''
Python 7 nodarbības mājasdarbs Nr.2

Uzdevums: aizpildīt vietas ar atzīmi TODO

Izveidot klasi, kura pārveido 5. nodarbības mājasdarbu Nr. 3 saturu par klasi
'''

import cv2
import numpy as np

class IntroOpenCV:
    '''
    Izveidot klasi, kurai ir 5 publiskas metodes:
    - setBilde -  definē bildes failu
    - bilde 
    - melnbalts
    - EdgeDetection
    - ZilsSarkans

    !Klasei nav neviena publiski pieejami parametri!
    '''
    def set_picture(self, BildeFails):
        self.__bilde = cv2.imread(BildeFails)

    def get_picture(self):
        # izsaucot šo metodi izvada Originālbildi . Originālbilde self.__bilde
        cv2.imshow('image', self.__bilde)
        cv2.waitKey(0)

    def get_black_white(self):
        # izsaucot šo metodi izvada melnbaltu bildi. Originālbilde self.__bilde
        img_melnbalts = cv2.cvtColor(self.__bilde, cv2.COLOR_BGR2GRAY)
        cv2.imshow('image', img_melnbalts)
        cv2.waitKey(0)
        return 0

    def get_edge_detection(self):
        # izsaucot šo metodi izvada bildi ar Caddy edge detection. Originālbilde self.__bilde
        img_caddy = cv2.Canny(self.__bilde, 10, 200)
        cv2.imshow('image', img_caddy)
        cv2.waitKey(0)

    def get_blue_red(self):
        # izsaucot šo metodi izvada bildi, kura apmaina zilo krāsu ar sarkanu. Originālbilde self.__bilde
        img_zils_sarkans = self.__bilde.copy()
        hsv = cv2.cvtColor(img_zils_sarkans, cv2.COLOR_BGR2HSV)
        lower_range = np.array([110,50,50])
        upper_range = np.array([130,255,255])
        mask = cv2.inRange(hsv, lower_range, upper_range)
        img_zils_sarkans[mask != 0] = [0,0,255]
        cv2.imshow('image', img_zils_sarkans)
        cv2.waitKey(0)



if __name__ == "__main__":
    obj = IntroOpenCV()
    obj.set_picture("python.jpg")
