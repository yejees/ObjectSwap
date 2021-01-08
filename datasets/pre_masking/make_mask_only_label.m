clear; close all; clc;

obj_name = 'mbn_bottle2';

label_folder = 'mbn_bottle2_label';

load_dir = sprintf('%s_label', obj_name);
save_dir = sprintf('%s_seg',   obj_name);

mkdir(save_dir);

img_size = 512;

file_list = dir(fullfile(load_dir, '*.png'));
n_img = length(file_list);
label_whole = zeros(img_size, img_size, 3, n_img);

for k = 1 : n_img
    labeldum = imresize(imread(sprintf('%s/%s', load_dir, file_list(k).name)), [img_size, img_size]);
    label_whole(:, :, :, k) = labeldum;
end

for k = 1 : n_img
    fprintf(sprintf('%d/%d\n', k, n_img));
    
    mask_dum = zeros(img_size, img_size);
    label_dum = label_whole(:,:,:,k);
    
    line_dum = uint8(zeros(size(label_dum)));
    
    mask_dum(label_dum(:,:,1)>160) = mask_dum(label_dum(:,:,1)>160) + 1;
    mask_dum(label_dum(:,:,2)>160) = mask_dum(label_dum(:,:,2)>160) + 1;
    mask_dum(label_dum(:,:,3)>160) = mask_dum(label_dum(:,:,3)>160) + 1;
    
    mask_dum(mask_dum==0) = 0;
    mask_dum(mask_dum>=1) = 1;
    mask_dum = imfill(mask_dum);

    imwrite(mask_dum,  sprintf('%s/%s_0.png', save_dir, file_list(k).name(1:end-4)));
end