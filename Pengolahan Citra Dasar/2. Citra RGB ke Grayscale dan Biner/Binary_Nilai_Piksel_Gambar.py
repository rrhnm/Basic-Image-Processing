# Mengimpor modul OpenCV
import cv2 as cv

# Mengimpor gambar
img = cv.imread("D:/ideapadGAMING/Download/Gambar.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Mengatur nilai ambang dan nilai maksimum
thresh = 127
max_value = 255

# Mengubah nilai ambang pada gambar grayscale
ret, thresh_img = cv.threshold(gray, thresh, max_value, cv.THRESH_BINARY)

# Menampilkan gambar grayscale dalam window terpisah
cv.imshow("Grayscale Image", gray)
cv.imshow("Threshold Image", thresh_img)

# Membuat fungsi untuk menampilkan nilai biner pada titik koordinat ketika mouse diklik
def show_binary(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        # Mendapatkan nilai biner pada titik koordinat
        binary_value = thresh_img[y, x]
        print("Koordinat [{}, {}]".format(x, y), end = " --> ")
        # Menampilkan nilai biner pada titik koordinat
        text = "Binary [{}]".format(binary_value // 255)
        print(text)

# Menampilkan gambar normal
cv.imshow("image", img)

cv.setMouseCallback("Threshold Image", show_binary)

cv.waitKey(0)
cv.destroyAllWindows()