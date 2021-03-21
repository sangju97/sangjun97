# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 08:20:42 2021

https://opencv-python.readthedocs.io/en/latest/doc/01.imageStart/imageStart.html

@author: DeskTop
"""

"""
homework: resize all imgs in the directory with new (w, h)
make a function with default arguments (w = 300, h = 300)
save each file with suffix (fn_resized.jpg)
make a function to check all new images in the directory 
(with timedelay = default argument:2000)
hint: import glob # imgs = glob.glob("*.jpg")

"""

import cv2
import glob


for image in glob.glob('*.jpg'):

    fname = image
    img_gray = cv2.imread(fname, 0) # 0: gray; 1, RGB; -1: transparency
    img_color = cv2.imread(fname, 1)
    
    
    
    #w_new = img_gray.shape[0]//2 # 1000
    #h_new = img_gray.shape[1]//2 # 500
    img_gnew = cv2.resize(img_gray, (300,300))
    img_cnew = cv2.resize(img_color, (300,300))
    
    # cv2.imshow('Gray', img_gray)
    # cv2.imshow('Color', img_color)
    cv2.imshow('Gray', img_gnew)
    cv2.imshow('Color', img_cnew)
    

    fname_new = image + "_resized.jpg"
    cv2.imwrite(fname_new, img_cnew)
    cv2.waitKey(2000) # 0: press button; 2000: 2 seconds
    cv2.destroyAllWindows()

