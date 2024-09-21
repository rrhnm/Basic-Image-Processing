import cv2 as cv
#Kuciyose Gambar
citra = cv.imread("D:/ideapadGAMING/Download/Gambar.jpg")
cv.imshow("Citra Awal", citra) #Menampilkan gambar

#RESIZE
height, width = 400, 500
resize_citra = cv.resize(citra, (width, height), interpolation = cv.INTER_AREA)
cv.imshow("Resize Citra", resize_citra)
cv.waitKey(0)