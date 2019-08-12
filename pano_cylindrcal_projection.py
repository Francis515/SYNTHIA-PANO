import numpy as np
import cv2
#change the parameters to adjust distortion degree and center.
#img: the input image, f: focal length, center_ratio: projection center(W/center_ratio_x, H/center_ratio_y)
def cylind_prj(img,  f, center_ratio_x=2, center_ratio_y=2):
    img_prj = np.zeros_like(img)
    
    fx = lambda x:f*np.arctan(x/f)
    fy = lambda x,y:y*np.cos(np.arctan(x/f))
    
    rows,cols = img.shape[0], img.shape[1]
    shift_x = int(cols/center_ratio_x)
    shift_y = int(rows/center_ratio_y)
    
    for oy in range(rows):
        for ox in range(cols):
            y = oy - shift_y
            x = ox - shift_x
            y_prj = int(fy(x,y)) +shift_y
            x_prj = int(fx(x)) + shift_x
            x_img = x + shift_x
            y_img = y + shift_y
            if x_prj<cols and x_img<cols and y_prj<rows and y_img<rows: 
                img_prj[y_prj][x_prj] = img[y_img][x_img]
            else:
                pass
            
            pass
        pass
    return img_prj

def synthia_prj(img):
    #range_w = 139
    #f = 637.7
    range_w = 173
    f = 532.740352

    center_x = 2
    center_y = 2
    img_h, img_w = img.shape[0], img.shape[1]

    img_p=cylind_prj(img,f,center_x,center_y)
    #img_p=img_p[:,range_w:img_w-range_w+1]
    img_p = img_p[:, range_w:img_w - range_w]
    return img_p




