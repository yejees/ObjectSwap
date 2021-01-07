clear; close all; clc;

object_name = 'mbn_bottle1';

load_dir      = object_name;
load_dir_seg  = sprintf('%s_seg', object_name);
% load_dir_out  = sprintf('%s_out', object_name);

save_dir = sprintf('../imaginaire/dataset/%s_no_out', object_name);

if exist(save_dir, 'dir')
    rmdir(save_dir, 's');
end

mkdir(sprintf('%s/images', save_dir));
mkdir(sprintf('%s/maps',   save_dir));

file_list      = dir(fullfile(load_dir,     '*.png'));
file_list_seg  = dir(fullfile(load_dir_seg, '*.png'));

img_size = 512;

for k = 1 : length(file_list)
    fprintf(sprintf('%d/%d\n', k, length(file_list)));
    img = imresize(imread(sprintf('%s/%s', load_dir,     file_list(k).name)),     [img_size, img_size], 'cubic');
    seg = imresize(imread(sprintf('%s/%s', load_dir_seg, file_list_seg(k).name)), [img_size, img_size], 'cubic');
    
    seg = seg / 255;
    
    tmp = uint8(ones(size(seg))) - uint8(seg);
    img_bg = img.*tmp;
    
    img_bg(img_bg>255) = 255;
    
    mkdir(sprintf('%s/images/seq%04d', save_dir, k));
    mkdir(sprintf('%s/maps/seq%04d',   save_dir, k));
    imwrite(img,    sprintf('%s/images/seq%04d/0001.png', save_dir, k));
    imwrite(img_bg, sprintf('%s/maps/seq%04d/0001.png',   save_dir, k));
end