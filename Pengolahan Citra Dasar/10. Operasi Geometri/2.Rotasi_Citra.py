import cv2 as cv
import imutils
#Kuciyose Gambar
citra = cv.imread("D:/ideapadGAMING/Download/Gambar.jpg")
cv.imshow("Citra Awal", citra) #Menampilkan gambar

#ROTASI
angle = -90
rotated = imutils.rotate(citra, angle)
cv.imshow("Rotasi Citra", rotated)
cv.waitKey(0)