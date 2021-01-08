clear; close all; clc;

folder_name = 'tmp';
obj_name = 'mbn_bottle2';

label_dir  = sprintf('%s/%s/label', folder_name, obj_name);

save_dir2  = sprintf('%s/%s/mask',  folder_name, obj_name);

mkdir(save_dir2);

img_size = 512;

file_list = dir(fullfile(label_dir, '*.jpg'));
n_img = length(file_list);
label_whole = zeros(img_size, img_size, n_img);

for k = 1 : n_img
    labeldum = imresize(imread(sprintf('%s/%s', label_dir, file_list(k).name)), [img_size, img_size]);
    label_whole(:, :, k) = labeldum;
end

mask_whole = zeros(img_size, img_size, n_img);

for k = 1 : n_img
    fprintf(sprintf('%d/%d\n', k, n_img));
    
    mask_dum  = zeros(img_size, img_size);
    label_dum = label_whole(:,:,k);

    mask_dum(label_dum>170) = mask_dum(label_dum>170) + 1;
    
    mask_dum(mask_dum~=1) = 0;
    mask_dum(mask_dum==1) = 1;
    mask_dum = imfill(mask_dum);
    
    mask_whole(:,:,k) = mask_dum;

    imwrite(mask_dum, sprintf('%s/%s_0.png', save_dir2, file_list(k).name(1:end-4)));
end