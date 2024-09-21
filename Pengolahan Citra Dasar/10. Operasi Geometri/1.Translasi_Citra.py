import cv2 as cv
import imutils
#Kuciyose Gambar
citra = cv.imread("D:/ideapadGAMING/Download/Gambar.jpg")
cv.imshow("Citra Awal", citra) #Menampilkan gambar

#TRANSLASI (Pergeseran)
x, y = 100, 20
shifted = imutils.translate(citra, x, y)
cv.imshow("Translasi Citra", shifted)
cv.waitKey(0)