import cv2 as cv
import numpy as np

citra = cv.imread("D:/ideapadGAMING/Download/Gambar.jpg")

MatriksSatu = np.ones(citra.shape, citra.dtype)*120

citraPengurangan = cv.subtract(citra, MatriksSatu)

cv.imshow('Citra Asli', citra)
cv.imshow('Citra Pengurangan', citraPengurangan)
cv.waitKey(0)