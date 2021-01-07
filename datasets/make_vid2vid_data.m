clear; close all; clc;

object_name = 'vitamin_aug3';

load_dir      = object_name;
load_dir_seg  = sprintf('%s_seg',  object_name);
load_dir_out  = sprintf('%s_out',  object_name);

save_dir = sprintf('../imaginaire/dataset/%s', object_name);

if exist(save_dir, 'dir')
    rmdir(save_dir, 's');
end

mkdir(sprintf('%s/train/images', save_dir));
mkdir(sprintf('%s/train/maps',   save_dir));
mkdir(sprintf('%s/val/images',   save_dir));
mkdir(sprintf('%s/val/maps',     save_dir));
mkdir(sprintf('%s/test/images',  save_dir));
mkdir(sprintf('%s/test/maps',    save_dir));

file_list      = dir(fullfile(load_dir,      '*.png'));
% file_list_seg  = dir(fullfile(load_dir_seg,  '*.png'));
% file_list_out  = dir(fullfile(load_dir_out,  '*.png'));

num_data = length(file_list);
num_train = round(0.85 * num_data);
num_val   = round(0.05 * num_data);
num_test  = num_data - num_train - num_val;

ind_list = randperm(num_data);

file_list     = file_list(ind_list);
% file_list_seg = file_list_seg(ind_list);
% file_list_out = file_list_out(ind_list);

for k = 1 : num_data
    k
    img  = imread(sprintf('%s/%s', load_dir,      file_list(k).name));
    seg  = imread(sprintf('%s/%s', load_dir_seg,  file_list(k).name));
    out  = imread(sprintf('%s/%s', load_dir_out,  file_list(k).name));

    tmp = uint8(ones(size(seg))) - uint8(seg);
    img_bg = img.*tmp;
    img_bg = img_bg + uint8(seg).*out;
    
    if k <= num_train
        mkdir(sprintf('%s/train/images/seq%04d', save_dir, k));
        mkdir(sprintf('%s/train/maps/seq%04d',   save_dir, k));
        imwrite(img,    sprintf('%s/train/images/seq%04d/0001.png', save_dir, k));
%         imwrite(img,    sprintf('%s/train/maps/seq%04d/0001.png',   save_dir, k));
        imwrite(img_bg, sprintf('%s/train/maps/seq%04d/0001.png',   save_dir, k));
    elseif k <= num_train + num_val
        mkdir(sprintf('%s/val/images/seq%04d',   save_dir, k));
        mkdir(sprintf('%s/val/maps/seq%04d',     save_dir, k));
        imwrite(img,    sprintf('%s/val/images/seq%04d/0001.png',   save_dir, k));
%         imwrite(img,    sprintf('%s/val/maps/seq%04d/0001.png',   save_dir, k));
        imwrite(img_bg, sprintf('%s/val/maps/seq%04d/0001.png',     save_dir, k));
    else
        mkdir(sprintf('%s/test/images/seq%04d',  save_dir, k));
        mkdir(sprintf('%s/test/maps/seq%04d',    save_dir, k));
        imwrite(img,    sprintf('%s/test/images/seq%04d/0001.png',  save_dir, k));
%         imwrite(img,    sprintf('%s/test/maps/seq%04d/0001.png',   save_dir, k));
        imwrite(img_bg, sprintf('%s/test/maps/seq%04d/0001.png',    save_dir, k));
    end
end