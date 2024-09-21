#Mengimpor modul OpenCV
import cv2 as cv

# Mengimpor gambar
img = cv.imread("D:/ideapadGAMING/Download/Gambar.jpg")

# Membuat fungsi untuk menampilkan nilai RGB pada titik koordinat ketika mouse diklik
def show_rgb(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        # Mendapatkan nilai RGB pada titik koordinat
        b, g, r = img[y, x]
        print("Koordinat [{}, {}]".format(x, y), end = " --> ")
        # Menampilkan nilai RGB pada titik koordinat
        text = "RGB [{}, {}, {}]".format(r, g, b)
        print(text)
        cv.imshow("image", img)

# Menampilkan gambar
cv.imshow("image", img)
cv.setMouseCallback("image", show_rgb)

cv.waitKey(0)
cv.destroyAllWindows()