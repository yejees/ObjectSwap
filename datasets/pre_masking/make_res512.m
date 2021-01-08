clear; close all; clc;

root_dir_load = 'TOTAL';
root_dir_save = 'TOTAL_512';

obj_name = 'pepsi';

img_dir_load = sprintf('%s/%s',     root_dir_load, obj_name);
seg_dir_load = sprintf('%s/%s_seg', root_dir_load, obj_name);

img_dir_save = sprintf('%s/%s',     root_dir_save, obj_name);
seg_dir_save = sprintf('%s/%s_seg', root_dir_save, obj_name);

mkdir(img_dir_save);
mkdir(seg_dir_save);

img_size = 512;

file_list_img = dir(fullfile(img_dir_load, '*.png'));
n_img = length(file_list_img);
for k = 1 : n_img
    fprintf('%d/%d for img\n', k, n_img);
    img = imresize(imread(sprintf('%s/%s', img_dir_load, file_list_img(k).name)), [img_size, img_size]);
    imwrite(img, sprintf('%s/%s.png', img_dir_save, file_list_img(k).name(1:end-4)));
end


file_list_seg = dir(fullfile(seg_dir_load, '*.png'));
n_seg = length(file_list_seg);
for k = 1 : n_seg
    fprintf('%d/%d for seg\n', k, n_seg);
    seg = imresize(imread(sprintf('%s/%s', seg_dir_load, file_list_seg(k).name)), [img_size, img_size]);
    imwrite(seg, sprintf('%s/%s.png', seg_dir_save, file_list_seg(k).name(1:end-4)));
end