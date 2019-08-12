import numpy as np
from skimage import io
import cv2

color_dict_SYN = {
    0:(0,0,0),
    1:(128,128,128),
    2:(128,0,0),
    3:(128,64,128),
    4:(0,0,192),
    5:(64,64,128),
    6:(128,128,0),
    7:(192,192,128),
    8:(64,0,128),
    9:(192,128,128),
    10:(64,64,0),
    11:(0,128,192),
    12:(0,172,0),
    13:(0,0,0),
    14:(0,0,0),
    15:(0,128,128)
}
def cvt2color(img,labels = 22):
    img_h,img_w = img.shape[0],img.shape[1]
    temp = np.zeros((img_h,img_w,3))
    for x in range(img_w):
        for y in range(img_h):
            trainId = img[y][x]
            if labels==22:
                pass
                #temp[y][x] = list(trainId2label[trainId].color)
            elif labels  == 16:
                temp[y][x] = color_dict_SYN[int(trainId)]
    temp = temp.astype(np.uint8)           
    return temp

