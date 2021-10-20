import cv2 as cv

img = cv.imread('resources/messi_large.jpg', cv.IMREAD_UNCHANGED)
print('Original Dimensions : ', img.shape)
print('Original Dimensions [100, 100] : ', img[100, 100])

scale_percent = 10
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

resized = cv.resize(img, dim, interpolation=cv.INTER_BITS)
print('Resized Dimensions : ', resized.shape)
print('Resized Dimensions [100, 100] : ', resized[100, 100])

cv.imshow('Resized Image',resized)
cv.waitKey(0)
cv.destroyAllWindows()