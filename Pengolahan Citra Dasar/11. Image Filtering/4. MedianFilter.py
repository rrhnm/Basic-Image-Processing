import cv2 as cv

citra = cv.imread("D:/ideapadGAMING/Download/Gambar.jpg")

# Apply the filter
median = cv.medianBlur(citra,5)

cv.imshow('Citra Asli', citra)
cv.imshow('Citra Median Blurring', median)
cv.waitKey(0)
cv.destroyAllWindows()