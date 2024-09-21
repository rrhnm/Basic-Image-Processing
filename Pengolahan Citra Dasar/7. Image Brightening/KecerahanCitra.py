import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

citra = cv.imread("D:/ideapadGAMING/Download/Gambar.jpg") #Membaca citra

# Meningkatkan kecerahan
citra_bright = cv.convertScaleAbs(citra, alpha=1.0, beta=40)

cv.imshow("Asli", citra)
cv.imshow("Kecerahan", citra_bright)

plt.figure(figsize=(10, 10))

plt.subplot(121), plt.hist(citra.ravel(), 256, [0, 256], color = 'black'), plt.title('Original')
plt.subplot(122), plt.hist(citra_bright.ravel(), 256, [0, 256], color = 'black'), plt.title('Kecerahan')

plt.show()

cv.waitKey(0) #Agar tidak langsung keluar
cv.destroyAllWindows()