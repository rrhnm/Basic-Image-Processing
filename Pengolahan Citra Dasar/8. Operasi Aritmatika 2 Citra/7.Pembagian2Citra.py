import cv2 as cv
import numpy as np

citra = cv.imread("D:/ideapadGAMING/Download/Gambar.jpg")
citra2 = cv.imread("D:/ideapadGAMING/Download/Gambar2.jpg")

citraPembagian =  cv.divide(citra, citra2)

cv.imshow('Citra Asli 1', citra)
cv.imshow('Citra Asli 2', citra2)
cv.imshow('Citra Pembagian', citraPembagian)
cv.waitKey(0)