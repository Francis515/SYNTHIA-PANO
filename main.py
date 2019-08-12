import numpy as np
import cv2
import os
import glob
from tqdm import trange
from pano_cylindrcal_projection import cylind_prj,synthia_prj
from pano_synthia import pano_stitch

def load_label(path):
    img=cv2.imread(path, -cv2.IMREAD_ANYDEPTH)
    label = img[:,:,2]
    return label

input_filepath = 'D:/dataset/Synthia/SYNTHIA-SEQS-05-SUMMER'
output_filepath = 'D:/dataset/End/Imgs'
mode1 = 'RGB'
mode2 = 'LABELS'
cam_side = 'Stereo_Left'
filename = 'seqs05_summer'
filenum = 787

RGB_B_list = sorted(glob.glob(os.path.join(input_filepath,mode1,cam_side,'Omni_B/*')))
RGB_F_list = sorted(glob.glob(os.path.join(input_filepath,mode1,cam_side,'Omni_F/*')))
RGB_L_list = sorted(glob.glob(os.path.join(input_filepath,mode1,cam_side,'Omni_L/*')))
RGB_R_list = sorted(glob.glob(os.path.join(input_filepath,mode1,cam_side,'Omni_R/*')))

LABELS_B_list = sorted(glob.glob(os.path.join(input_filepath,'GT',mode2,cam_side,'Omni_B/*')))
LABELS_F_list = sorted(glob.glob(os.path.join(input_filepath,'GT',mode2,cam_side,'Omni_F/*')))
LABELS_L_list = sorted(glob.glob(os.path.join(input_filepath,'GT',mode2,cam_side,'Omni_L/*')))
LABELS_R_list = sorted(glob.glob(os.path.join(input_filepath,'GT',mode2,cam_side,'Omni_R/*')))

for n in trange(0,filenum):
    #read the images
    RGB_B = cv2.imread(RGB_B_list[n])
    RGB_F = cv2.imread(RGB_F_list[n])
    RGB_L = cv2.imread(RGB_L_list[n])
    RGB_R = cv2.imread(RGB_R_list[n])

    #do img projection
    RGB_B = synthia_prj(RGB_B)
    RGB_F = synthia_prj(RGB_F)
    RGB_L = synthia_prj(RGB_L)
    RGB_R = synthia_prj(RGB_R)

    #random order to stitch
    img = [RGB_L,RGB_F,RGB_R,RGB_B]
    st = np.random.randint(4)
    #st = 3
    pano_img = pano_stitch(img[st%4],img[(st+1)%4],img[(st+2)%4],img[(st+3)%4],type='train')
    img_name = output_filepath+'/RGB/'+filename+'/'+filename+'_pano_'+str(n)+'.png'
    cv2.imwrite(img_name,pano_img)

    #read the labels
    LABEL_B = load_label(LABELS_B_list[n])
    LABEL_F = load_label(LABELS_F_list[n])
    LABEL_L = load_label(LABELS_L_list[n])
    LABEL_R = load_label(LABELS_R_list[n])
    #do label projection
    LABEL_B = synthia_prj(LABEL_B)
    LABEL_F = synthia_prj(LABEL_F)
    LABEL_L = synthia_prj(LABEL_L)
    LABEL_R = synthia_prj(LABEL_R)
    #stitch by order the same as img
    label = [LABEL_L,LABEL_F,LABEL_R,LABEL_B]
    pano_label = pano_stitch(label[st%4],label[(st+1)%4],label[(st+2)%4],label[(st+3)%4],type='label')
    label_name = output_filepath+'/LABELS/'+filename+'/'+filename+'_label_'+str(n)+'.png'
    cv2.imwrite(label_name,pano_label)



