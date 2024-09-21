#Mengimpor modul OpenCV
import cv2 as cv

# Mengimpor gambar
img = cv.imread("D:/ideapadGAMING/Download/Gambar.jpg")
# Mengonversi gambar jadi keabuan
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Menampilkan gambar grayscale dalam window terpisah
cv.imshow("Grayscale Image", gray)
# Membuat fungsi untuk menampilkan nilai RGB pada titik koordinat ketika mouse diklik
def show_gray(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        # Mendapatkan nilai grayscale pada titik koordinat
        gray_value = gray[y, x]
        print("Koordinat [{}, {}]".format(x, y), end = " --> ")
        # Menampilkan nilai grayscale pada titik koordinat
        text = "Grayscale [{}]".format(gray_value)
        print(text)
        cv.imshow("image", img)

# Menampilkan gambar normal
cv.imshow("image", img)

cv.setMouseCallback("Grayscale Image", show_gray)

cv.waitKey(0)
cv.destroyAllWindows()