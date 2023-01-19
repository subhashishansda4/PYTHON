# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 18:22:39 2022

@author: VAGUE
"""

import qrcode
import cv2

# generating qr code
img = qrcode.make('Decision defines Destiny')
img.save('temp.png')

# configuring qr code
qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("rick roll.png")

# reading qr code through opencv
img=cv2.imread("temp.png")
det=cv2.QRCodeDetector()
val, pts, st_code=det.detectAndDecode(img)
print(val)