import cv2 as cv
import numpy as np

citra = cv.imread("D:/ideapadGAMING/Download/Gambar.jpg")

MatriksSatu = np.ones(citra.shape, citra.dtype)*100

citraPenjumlahan = cv.add(citra, MatriksSatu)

cv.imshow('Citra Asli', citra)
cv.imshow('Citra Penjumlahan', citraPenjumlahan)
cv.waitKey(0)