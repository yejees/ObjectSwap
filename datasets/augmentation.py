import imgaug.augmenters as iaa
from glob import glob
import cv2
import os

load_dir_img = 'vitamin'
load_dir_seg = 'vitamin_seg'

save_dir_img = 'vitamin_aug3'
save_dir_seg = 'vitamin_aug3_seg'
save_dir_out = 'vitamin_aug3_out'

os.makedirs(save_dir_img, exist_ok=True)
os.makedirs(save_dir_seg, exist_ok=True)
os.makedirs(save_dir_out, exist_ok=True)

file_list_img = glob('%s/*.png' % load_dir_img)
file_list_seg = glob('%s/*.png' % load_dir_img)

aug1 = iaa.PerspectiveTransform(scale=(0, 0.15))
aug2 = iaa.Affine(scale={"x": (0.5, 1), "y": (0.5, 1)})
aug3 = iaa.Affine(translate_percent={"x": (-0.25, 0.25), "y": (-0.25, 0.25)})
aug4 = iaa.MultiplyBrightness((0.8, 1.2))
#aug4 = iaa.Affine(rotate=(-90, 90))
seq  = iaa.Sequential([aug1, aug2, aug3])
aug_num = 20

img_ind = 1
for file_path in file_list_img:
    print('%d/%d' % (img_ind, len(file_list_img)))
    file_name = os.path.basename(file_path)
    img = cv2.imread('%s/%s' % (load_dir_img, file_name))
    seg = cv2.imread('%s/%s_0.png' % (load_dir_seg,  file_name[:-4]))
    out = cv2.Canny(img, 30, 50)
    cv2.imwrite('%s/%s_aug00.png'   % (save_dir_img, file_name[:-4]), img)
    cv2.imwrite('%s/%s_aug00.png' % (save_dir_seg, file_name[:-4]), seg)
    cv2.imwrite('%s/%s_aug00.png'   % (save_dir_out, file_name[:-4]), out)
    
    for k in range(aug_num - 1):
        img_aug, seg_aug = seq(images=[img], segmentation_maps=[seg])
        out_aug = cv2.Canny(img_aug[0], 30, 50)
        cv2.imwrite('%s/%s_aug%02d.png' % (save_dir_img, file_name[:-4], k + 1), img_aug[0])
        cv2.imwrite('%s/%s_aug%02d.png' % (save_dir_seg, file_name[:-4], k + 1), seg_aug[0])
        cv2.imwrite('%s/%s_aug%02d.png' % (save_dir_out, file_name[:-4], k + 1), out_aug)
        
    img_ind += 1