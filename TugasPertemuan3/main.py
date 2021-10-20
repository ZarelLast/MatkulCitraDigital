import cv2 as cv
import matplotlib.pyplot as plt
import copy 

def cetak(fileImg, judul):
  # plt.imshow(cv.cvtColor(fileImg, cv.COLOR_BGR2RGB))
  # plt.get_current_fig_manager().canvas.manager.set_window_title(judul)
  # plt.show()
  # tanpa matlib
  cv.imshow(judul, fileImg)
  cv.waitKey(0)
  cv.destroyAllWindows()

img = cv.imread('resources/soccer_kid_large.jpg', cv.IMREAD_UNCHANGED)

scale_percent = 60
width = int(img.shape[1] * scale_percent / 100)
heigth = int(img.shape[0] * scale_percent / 100)
dim = (width, heigth)

resized = cv.resize(img, dim, interpolation=cv.IMREAD_COLOR)
cv.imwrite('resources/soccer_kid_small.jpg',resized)

double_ball = copy.deepcopy(resized)
# ROI bola 750:860, 785:895
bola = double_ball[750:860, 785:895]
# ROI duplikat bola 795:905, 70:180
double_ball[795:905, 70:180] = bola
nim = '5200411416'
cv.putText(double_ball, nim, (1000, 880), cv.FONT_HERSHEY_SIMPLEX, 2, (0,0,0), 5)
cv.imwrite('resources/soccer_kid_small_doubleBall.jpg',double_ball)

print("Ukuran asli:", img.shape)
print("Ukuran mini:", resized.shape)

cetak(resized, 'Resized Image')
cetak(double_ball, 'Resized Image Double Ball')