import cv2 as cv

citra = cv.imread("D:/ideapadGAMING/Download/Gambar.jpg")
citra2 = cv.imread("D:/ideapadGAMING/Download/Gambar2.jpg")

citraOR =  cv.bitwise_or(citra, citra2)

cv.imshow('Citra Asli 1', citra)
cv.imshow('Citra Asli 2', citra2)
cv.imshow('Citra OR', citraOR)
cv.waitKey(0)