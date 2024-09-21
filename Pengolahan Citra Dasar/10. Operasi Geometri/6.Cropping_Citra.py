import cv2 as cv
#Kuciyose Gambar
citra = cv.imread("D:/ideapadGAMING/Download/Gambar.jpg")
cv.imshow("Citra Awal", citra) #Menampilkan gambar

#CROPPING
kepala_capy = citra[40:220, 250:500]
cv.imshow("Kepala Capy", kepala_capy)
cv.waitKey(0)