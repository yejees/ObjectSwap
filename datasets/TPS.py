import numpy as np
import cv2

import scipy.io as sio
import os
from glob import glob
from utils import WarpImage_TPS

src_dir = 'mbn_bottle2' 
trg_dir = 'vitamin_sample'
lm_dir  = src_dir + '_lm'

save_dir = '%s_out' % src_dir

os.makedirs(save_dir, exist_ok=True)

file_list_lm = sorted(glob('%s/*.mat' % lm_dir))

lm1_x = sio.loadmat('%s/0008_lm.mat' % trg_dir)['x'][:,0]
lm1_y = sio.loadmat('%s/0008_lm.mat' % trg_dir)['y'][:,0]
lm1 = []
for i in range(len(lm1_x)):
    lm1.append([lm1_x[i], lm1_y[i]])
lm1 = np.array(lm1)

img = cv2.imread('%s/0008.png' % trg_dir)

for file_dir in file_list_lm:
    filename = os.path.basename(file_dir)
    lm2_x = sio.loadmat(file_dir)['x'][:,0]
    lm2_y = sio.loadmat(file_dir)['y'][:,0]
    lm2 = []
    
    for i in range(len(lm2_x)):
        lm2.append([lm2_x[i], lm2_y[i]])
    lm2 = np.array(lm2)
    
    img_warp = WarpImage_TPS(lm1, lm2, img)
    
    img_warp_canny = cv2.Canny(img_warp, 30, 50)

    cv2.imwrite('%s/%s.png' % (save_dir, filename[:-4]), img_warp_canny)