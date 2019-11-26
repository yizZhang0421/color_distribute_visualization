import cv2
img=cv2.imread('wcs-chart-4x.png', cv2.IMREAD_UNCHANGED)
img=img[:,:,0:3]

start_x=304
gap_x=80+12
start_y=250
gap_y=100+16
color_chart=list()
for i in range(8):
    data=[]
    for j in range(40):
        #img[start_y-10:start_y+10, start_x-10:start_x+10, :]=0
        data.append(img[start_y][start_x])
        start_x+=gap_x
    color_chart.append(data)
    start_x-=40*gap_x
    start_y+=gap_y
cv2.imwrite('test.jpg', img)

import numpy as np
chart=np.zeros([8*25, 40*20, 3], dtype=np.uint8)
start_r=0
gap_r=25
start_c=0
gap_c=20
for i in range(8):
    for j in range(40):
        chart[start_r:start_r+gap_r, start_c:start_c+gap_c, :]=np.full((25, 20, 3), color_chart[i][j])
        start_c+=gap_c
    start_c-=40*gap_c
    start_r+=gap_r
cv2.imwrite('test.jpg', chart)

cv2.imshow('test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()