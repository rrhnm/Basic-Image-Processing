import cv2 as cv
import numpy as np

citra = cv.imread("D:/ideapadGAMING/Download/Gambar.jpg")

MatriksSatu = np.ones(citra.shape, citra.dtype)*2

citraPengurangan = cv.multiply(citra, MatriksSatu)

cv.imshow('Citra Asli', citra)
cv.imshow('Citra Pembagian', citraPengurangan)
cv.waitKey(0)