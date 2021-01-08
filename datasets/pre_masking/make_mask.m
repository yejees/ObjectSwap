clear; close all; clc;

folder_name = 'new_label';
obj_name = 'vitamin';

label_dir  = sprintf('%s/%s/label',      folder_name, obj_name);
img_dir    = sprintf('%s/%s/png',        folder_name, obj_name);

save_dir1  = sprintf('%s/%s/png_resize', folder_name, obj_name);
save_dir2  = sprintf('%s/%s/mask',       folder_name, obj_name);
save_dir3  = sprintf('%s/%s/outline',       folder_name, obj_name);

mkdir(save_dir1);
mkdir(save_dir2);
mkdir(save_dir3);

img_size = 512;

file_list = dir(fullfile(label_dir, '*.png'));
n_img = length(file_list);
label_whole = zeros(img_size, img_size, 3, n_img);

for k = 1 : n_img
    labeldum = imresize(imread(sprintf('%s/%s', label_dir, file_list(k).name)), [img_size, img_size]);
    label_whole(:, :, :, k) = labeldum;
end

for k = 1 : n_img
    img = imresize(imread(sprintf('%s/%s', img_dir, file_list(k).name)), [img_size, img_size]);
    imwrite(img, sprintf('%s/%s.png', save_dir1, file_list(k).name(1:end-4)));
end

mask_whole = zeros(img_size, img_size, n_img);
line_whole = zeros(img_size, img_size, n_img);

for k = 1 : n_img
    fprintf(sprintf('%d/%d\n', k, n_img));
    
    mask_dum = zeros(img_size, img_size);
    label_dum = label_whole(:,:,:,k);
    
    line_dum = uint8(zeros(size(label_dum)));
    
%     if k == 226
%         label_dum(368, 257, :) = 200;
%         label_dum(368, 258, :) = 200;
%     end
    
    mask_dum(label_dum(:,:,1)>160) = mask_dum(label_dum(:,:,1)>160) + 1;
    mask_dum(label_dum(:,:,2)>160) = mask_dum(label_dum(:,:,2)>160) + 1;
    mask_dum(label_dum(:,:,3)>160) = mask_dum(label_dum(:,:,3)>160) + 1;
    
    mask_dum(mask_dum==0) = 0;
    mask_dum(mask_dum>=1) = 1;
    mask_dum = imfill(mask_dum);
    
    line_dum(label_dum>160) = label_dum(label_dum>160);    

    imwrite(mask_dum,  sprintf('%s/%s_0.png', save_dir2, file_list(k).name(1:end-4)));
    imwrite(line_dum, sprintf('%s/%s.png',    save_dir3, file_list(k).name(1:end-4)));
end