import cv2 as cv

citra = cv.imread("D:/ideapadGAMING/Download/Gambar.jpg") #Membaca citra
citra_negatif = 255 - citra
cv.imshow("Citra Awal",citra) #Menampilkan citra
cv.imshow("Citra Negatif",citra_negatif) #Menampilkan citra negatif

cv.waitKey(0) #Agar tidak langsung keluar