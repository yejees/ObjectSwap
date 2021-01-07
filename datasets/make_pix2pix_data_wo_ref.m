clear; close all; clc;

object_name = 'vitamin';

load_dir      = object_name;
load_dir_seg  = sprintf('%s_seg',  object_name);
load_dir_out  = sprintf('%s_out_wo_ref',  object_name);
% load_dir_out2 = sprintf('%s_out2', object_name);

save_dir = sprintf('../pytorch-CycleGAN-and-pix2pix/datasets/%s_pix2pix_out_wo_ref', object_name);

if exist(save_dir, 'dir')
    rmdir(save_dir, 's');
end

mkdir(sprintf('%s/train', save_dir));
mkdir(sprintf('%s/val',   save_dir));
mkdir(sprintf('%s/test',  save_dir));

file_list      = dir(fullfile(load_dir,      '*.png'));
file_list_seg  = dir(fullfile(load_dir_seg,  '*.png'));
file_list_out  = dir(fullfile(load_dir_out,  '*.png'));
% file_list_out2 = dir(fullfile(load_dir_out2, '*.png'));

num_data = length(file_list);
num_train = round(0.85 * num_data);
num_val   = round(0.05 * num_data);
num_test  = num_data - num_train - num_val;

ind_list = randperm(num_data);

file_list     = file_list(ind_list);
file_list_seg = file_list_seg(ind_list);
file_list_out = file_list_out(ind_list);

for k = 1 : num_data
% for k = 1 : 94
    k
    img  = imread(sprintf('%s/%s', load_dir,      file_list(k).name));
    seg  = imread(sprintf('%s/%s', load_dir_seg,  file_list_seg(k).name));
    out  = imread(sprintf('%s/%s', load_dir_out,  file_list_out(k).name));
%     out2 = imread(sprintf('%s/%s', load_dir_out2, file_list_out2(k).name));
    
%     tmp = repmat(uint8(ones(size(seg))) - uint8(seg), [1,1,3]);
    tmp = uint8(ones(size(seg))) - uint8(seg);
    img_bg = img.*tmp;
%     img_bg = img_bg + uint8(seg).*out2 + uint8(seg).*out/2;
    img_bg = img_bg + uint8(seg).*out;
    
%     img_bg(img_bg>255) = 255;
    
    img_cat = cat(2, img_bg, img);
    
    if k <= num_train
        imwrite(img_cat, sprintf('%s/train/%04d.png', save_dir, k));
    elseif k <= num_train + num_val
        imwrite(img_cat, sprintf('%s/val/%04d.png',   save_dir, k));
    else
        imwrite(img_cat, sprintf('%s/test/%04d.png',  save_dir, k));
    end
end