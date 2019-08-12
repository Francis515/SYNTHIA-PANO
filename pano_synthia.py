from skimage import io
import numpy as np

#803
def pano_stitch(l,f,r,b,type='train',edge =834):
    if not edge%2:
        edge=edge+1
    img_w = b.shape[1]
    half_w = img_w//2
    img_h = b.shape[0]
    pano_w = edge * 4
    pano_h = img_h
    if type=='train':
        pano = np.zeros((pano_h,pano_w,3))
    else:
        pano = np.zeros((pano_h,pano_w))
    pano[:,0:edge]= l[:,half_w-edge//2:half_w+edge//2+1]
    pano[:,edge:2*edge]=f[:,half_w-edge//2:half_w+edge//2+1]
    pano[:,2*edge:3*edge]=r[:,half_w-edge//2:half_w+edge//2+1]
    pano[:,3*edge:4*edge]=b[:,half_w-edge//2:half_w+edge//2+1]
    pano = pano.astype(np.uint8)
    return pano
