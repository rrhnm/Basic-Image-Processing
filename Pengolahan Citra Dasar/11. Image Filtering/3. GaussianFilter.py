import cv2 as cv

citra = cv.imread("D:/ideapadGAMING/Download/Gambar.jpg")

gaussian = cv.GaussianBlur(citra,(5,5),0)

cv.imshow('Citra Asli', citra)
cv.imshow('Citra Gaussian Blurring', gaussian)
cv.waitKey(0)
cv.destroyAllWindows()
