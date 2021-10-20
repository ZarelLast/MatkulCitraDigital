import cv2 as cv
import numpy as np

canvas = np.ones((600, 800, 3), np.uint8) * 255

def identitas(context, x, y, font_size, font_color):
  cv.putText(canvas, context, (x, y), cv.FONT_HERSHEY_SIMPLEX, font_size, font_color, 2)

def box(x1,x2,y1,y2,color):
  cv.rectangle(canvas, (x1,y1), (x2,y2), color, -1)

def wheel(x,y,r,color):
  cv.circle(canvas, (x,y), r, color, -1)

def poly(pts, color):
  cv.fillPoly(canvas, [np.array(pts)], color)

# badan
poly([[230, 270], [500, 410], [100, 410], [230, 270]], (255,0,0))
box(230,500,270,410, (220,190,0))
box(500,670,160,410, (0,0,220))

# cerobong
box(290,340,190,270, (255,0,0))
box(275,355,150,190, (0,255,0))
poly([[275, 150], [290, 130], [340, 130], [355, 150], [275, 150]], (255,0,0))

# jendela
box(530,640,185,270, (100,100,100))
box(540,630,195,260, (0,0,0))

# roda 
wheel(280,445, 35, (112,112,112))
wheel(390,445, 35, (112,112,112))
wheel(585,420, 60, (112,112,112))
wheel(585,420, 35, (0,140,160))
cv.line(canvas, (280, 435), (585, 435), (0, 0, 0), 4)

# nama & nim
identitas("Muhammad Ilham Triwibowo", 460, 590, 0.75, (255,0,0))
identitas("5200411416", 640, 560, 0.75, (255,0,0))

cv.imshow("Kereta | 5200411416 - Muhammad Ilham Triwibowo", canvas)
cv.waitKey()

