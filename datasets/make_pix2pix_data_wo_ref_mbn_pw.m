clear; close all; clc;

object_name = 'mbn_bottle2';

load_dir      = object_name;
load_dir_seg  = sprintf('%s_seg', object_name);
load_dir_out  = sprintf('%s_out', object_name);

save_dir = sprintf('../pytorch-CycleGAN-and-pix2pix/datasets/%s_pix2pix_w_ref_vitamin_pw/test', object_name);
mkdir(save_dir);

file_list      = dir(fullfile(load_dir,     '*.png'));
file_list_seg  = dir(fullfile(load_dir_seg, '*.png'));
file_list_out  = dir(fullfile(load_dir_out, '*.png'));

img_size = 512;

for k = 1 : length(file_list)
    k
    img = imresize(imread(sprintf('%s/%s', load_dir,     file_list(k).name)),     [img_size, img_size], 'cubic');
    seg = imresize(imread(sprintf('%s/%s', load_dir_seg, file_list_seg(k).name)), [img_size, img_size], 'cubic');
    out = imresize(imread(sprintf('%s/%s', load_dir_out, file_list_out(k).name)), [img_size, img_size], 'cubic');
    
%     tmp = repmat(uint8(ones(size(seg))) - uint8(seg), [1,1,3]);
    tmp = uint8(ones(size(seg))) - uint8(seg);
    img_bg = img.*tmp;
%     img_bg = img_bg + uint8(seg).*out2 + uint8(seg).*out/2;
    img_bg = img_bg + uint8(seg).*out;
    
    img_bg(img_bg>255) = 255;
    
    img_cat = cat(2, img_bg, img);
    
    imwrite(img_cat, sprintf('%s/%s', save_dir, file_list(k).name));
end