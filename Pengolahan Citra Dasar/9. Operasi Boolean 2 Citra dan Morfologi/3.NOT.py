import cv2 as cv

citra = cv.imread("D:/ideapadGAMING/Download/Gambar.jpg")

citraNOT =  cv.bitwise_not(citra)

cv.imshow('Citra Asli', citra)
cv.imshow('Citra NOT', citraNOT)
cv.waitKey(0)