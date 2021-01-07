import numpy as np
import cv2

import scipy.io as sio
import os
from glob import glob

src_dir = 'mbn_bottle2' 
trg_dir = 'bottle_vitamin_samples'
lm_dir  = src_dir + '_lm2'

save_dir = '%s_seg_vitamin' % src_dir

os.makedirs(save_dir, exist_ok=True)

file_list_lm = sorted(glob('%s/*.mat' % lm_dir))

lm3_x = sio.loadmat('%s/vitamin_lm.mat' % trg_dir)['x'][:,0]
lm3_y = sio.loadmat('%s/vitamin_lm.mat' % trg_dir)['y'][:,0]
lm3 = []
for i in range(len(lm3_x)):
    if i == 3:
        ind = 2
    elif i== 2:
        ind = 3
    else:
        ind = i
    lm3.append([lm3_x[ind], lm3_y[ind]])
lm3 = np.array(lm3, dtype='float32')

img = cv2.imread('%s/vitamin_seg.jpg' % trg_dir)

(x,y,z) = img.shape

for file_dir in file_list_lm:
    filename = os.path.basename(file_dir)
    lm2_x = sio.loadmat('%s/%s' % (lm_dir, filename))['x'][:,0]
    lm2_y = sio.loadmat('%s/%s' % (lm_dir, filename))['y'][:,0]
    lm2 = []
    for i in range(len(lm2_x)):
        if i == 3:
            ind = 2
        elif i== 2:
            ind = 3
        else:
            ind = i
        lm2.append([lm2_x[ind], lm2_y[ind]])
    lm2 = np.array(lm2, dtype='float32')
    
    M = cv2.getPerspectiveTransform(lm3, lm2)
    dst = cv2.warpPerspective(img, M, (512, 512), flags=cv2.INTER_CUBIC)
    
    cv2.imwrite('%s/%s_0.png' % (save_dir, filename[:-4]), dst)