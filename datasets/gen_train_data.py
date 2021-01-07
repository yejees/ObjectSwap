from glob import glob
from shutil import copy2
import os
from random import shuffle

model_name = 'AttentionGAN'

folder_A1 = 'pepsi'

folder_B = 'vitamin'

num_data = 331 

dataset_name = '%s2%s_%d' % (folder_A1, folder_B, num_data)
save_dir = '../%s/datasets/%s' % (model_name, dataset_name)

os.makedirs(save_dir + '/trainA',     exist_ok=True)
os.makedirs(save_dir + '/trainB',     exist_ok=True)
os.makedirs(save_dir + '/trainA_seg', exist_ok=True)
os.makedirs(save_dir + '/trainB_seg', exist_ok=True)
os.makedirs(save_dir + '/valA',       exist_ok=True)
os.makedirs(save_dir + '/valB',       exist_ok=True)
os.makedirs(save_dir + '/valA_seg',   exist_ok=True)
os.makedirs(save_dir + '/valB_seg',   exist_ok=True)

os.makedirs(save_dir + '/testB',      exist_ok=True)
os.makedirs(save_dir + '/testB_seg',  exist_ok=True)

file_list_A1      = sorted(glob(folder_A1 +'/*.png'))
file_list_A1_seg  = sorted(glob(folder_A1 +'_seg/*.png'))

file_list_B       = sorted(glob(folder_B +'/*.png'))
file_list_B_seg   = sorted(glob(folder_B +'_seg/*.png'))

pair_A = []
for A1, A1_seg in zip(file_list_A1, file_list_A1_seg):
    pair_A.append([A1, A1_seg])
shuffle(pair_A)

pair_B = []
for B1, B1_seg in zip(file_list_B, file_list_B_seg):
    pair_B.append([B1, B1_seg])
shuffle(pair_B)

cnt_A = 1
for filenames in pair_A:
    copy2(filenames[0], '%s/trainA/%s.png'       % (save_dir, str(cnt_A).zfill(4)))
    copy2(filenames[0], '%s/valA/%s.png'         % (save_dir, str(cnt_A).zfill(4)))
    copy2(filenames[1], '%s/trainA_seg/%s_0.png' % (save_dir, str(cnt_A).zfill(4)))
    copy2(filenames[1], '%s/valA_seg/%s_0.png'   % (save_dir, str(cnt_A).zfill(4)))
    cnt_A += 1
    
#######
    
cnt_B = 1
for filenames in pair_B:
    copy2(filenames[0], '%s/trainB/%s.png'       % (save_dir, str(cnt_B).zfill(4)))
    copy2(filenames[0], '%s/valB/%s.png'         % (save_dir, str(cnt_B).zfill(4)))
    copy2(filenames[1], '%s/trainB_seg/%s_0.png' % (save_dir, str(cnt_B).zfill(4)))
    copy2(filenames[1], '%s/valB_seg/%s_0.png'   % (save_dir, str(cnt_B).zfill(4)))
    copy2(filenames[1], '%s/testB/%s_0.png'      % (save_dir, str(cnt_B).zfill(4)))
    copy2(filenames[1], '%s/testB_seg/%s_0.png'  % (save_dir, str(cnt_B).zfill(4)))
    cnt_B += 1