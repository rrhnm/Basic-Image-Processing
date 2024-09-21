import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

citra = cv.imread("D:/ideapadGAMING/Download/Gambar.jpg") #Membaca citra

b, g, r = cv.split(citra)

cv.imshow("Asli", citra)
cv.imshow("Blue", b)
cv.imshow("Green", g)
cv.imshow("r", r)

plt.figure(figsize=(10, 10))

plt.subplot(221), plt.hist(citra.ravel(), 256, [0, 256], color = 'black'), plt.title('Original')
plt.subplot(222), plt.hist(b.ravel(), 256, [0, 256], color = 'blue'), plt.title('Blue')
plt.subplot(223), plt.hist(g.ravel(), 256, [0, 256], color = 'green' ), plt.title('Green')
plt.subplot(224), plt.hist(r.ravel(), 256, [0, 256], color = 'red'), plt.title('Red')

plt.show()

cv.waitKey(0) #Agar tidak langsung keluar
cv.destroyAllWindows()