##canny edge detection
import cv2
#import os
import imageio as io

img_file_path = 'E:/AIPARK/HACKATHON/sample.jpg'
img_folder_path = 'E:/AIPARK/HACKATHON/vitamin/'
save_canny_30_50 = 'E:/AIPARK/HACKATHON/EDGE_DETECTION/canny_30_50/'
save_canny_100_200 = 'E:/AIPARK/HACKATHON/EDGE_DETECTION/canny_100_200/'


sample_img = cv2.imread(img_file_path)
sample_img = cv2.resize(sample_img, (512, 512))
sample_shape1 = cv2.Canny(sample_img, 30, 50)
sample_shape2 = cv2.Canny(sample_img, 100, 200)