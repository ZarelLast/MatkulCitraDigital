import cv2 as cv
import matplotlib.pyplot as plt

def cetak(fileImg, judul):
  plt.imshow(cv.cvtColor(fileImg, cv.COLOR_BGR2BGRA))
  print(judul)
  # cv.imshow(judul, fileImg)
  # cv.waitKey(0)
  # cv.destroyAllWindows()

img = cv.imread('resources/soccer_kid_large.jpg', cv.IMREAD_UNCHANGED)

scale_percent = 60
width = int(img.shape[1] * scale_percent / 100)
heigth = int(img.shape[0] * scale_percent / 100)
dim = (width, heigth)

resized = cv.resize(img, dim, interpolation=cv.IMREAD_COLOR)

cv.imwrite('resources/soccer_small.jpg',resized)

print("Ukuran asli:", img.shape)
print("Ukuran mini:", resized.shape)

cetak(img, 'Original Image')
cetak(resized, 'Resized Image')