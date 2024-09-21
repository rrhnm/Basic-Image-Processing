import cv2 as cv

citra = cv.imread('D:/ideapadGAMING/Download/Gambar.jpg') #Membaca citra
cv.imshow("Citra",citra) #Menampilkan citra

#Menampilkan Nilai Pixel Citra

print("Pixel Semua Citra")
print(citra, end = "/n/n") #Semua

print("Biru")
print(citra[:,:,0], end = "\n\n") #Biru saja

print("Hijau")
print(citra[:,:,1], end = "\n\n") #Hijau saja

print("Merah")
print(citra[:,:,2], end = "\n\n") #Merah

cv.waitKey(0) #Agar tidak langsung keluar