from glob import glob
from shutil import copy2
import os

folder_A = 'mbn_bottle2'
folder_B = 'vitamin'
folder_A_test = 'mbn_bottle2'
num_data = 416

dataset_name = '%s2%s_%d' % (folder_A, folder_B, num_data)
save_dir = '../instagan/datasets/%s' % (dataset_name)

os.makedirs(save_dir + '/testA',      exist_ok=True)
os.makedirs(save_dir + '/testA_seg',  exist_ok=True)

file_list_A_test     = sorted(glob(folder_A_test + '/*.png'))
file_list_A_test_seg = sorted(glob(folder_A_test + '_seg/*.png'))
    
for filename in file_list_A_test:
    name = filename.split('/')[-1]
    copy2(filename, '%s/testA/%s' % (save_dir, name))
    
for filename in file_list_A_test_seg:
    name = filename.split('/')[-1]
    copy2(filename, '%s/testA_seg/%s' % (save_dir, name))