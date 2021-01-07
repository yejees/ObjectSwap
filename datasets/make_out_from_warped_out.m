clear; close all; clc;

src_dir = 'vitamin_out_sample_warped2mbn_bottle2_little';
trg_dir = 'mbn_bottle2_little_out';

exist_th = 1;
th = 50;

file_list = dir(fullfile(src_dir, '*.png'));

for k = 1 : length(file_list)
    img = imread(sprintf('%s/%s', src_dir, file_list(k).name));
    img_th = img;
    
    if exist_th == 1
        img_th(img>=th) = 255;
        img_th(img< th) = 0;
    end
    
    imwrite(img_th, sprintf('%s/%s', trg_dir, file_list(k).name));
end