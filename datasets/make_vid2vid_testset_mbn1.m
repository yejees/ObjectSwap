clear; close all; clc;

object_name = 'mbn_bottle1';

load_dir      = object_name;
load_dir_seg  = sprintf('%s_seg', object_name);
save_dir = sprintf('../imaginaire/dataset/%s', object_name);

if exist(save_dir, 'dir')
    rmdir(save_dir, 's');
end

mkdir(sprintf('%s/images', save_dir));
mkdir(sprintf('%s/maps',   save_dir));

file_list = dir(fullfile(load_dir, '*.png'));

for k = 1 : length(file_list)
    fprintf(sprintf('%d/%d\n', k, length(file_list)));
    img =  imresize(imread(sprintf('%s/%s', load_dir, file_list(k).name)), [512, 512], 'cubic');
    if k < 77
        seg = imtranslate(imread('samples/0008_vitamin_0.png'), [15, -7], 'FillValues', 0);
        out = imtranslate(imread('samples/0008_vitamin_out_w_ref.png'), [15, -7], 'FillValues', 0);
    else
        seg = imtranslate(imread('samples/0008_vitamin_0.png'), [5, -15], 'FillValues', 0);
        out = imtranslate(imread('samples/0008_vitamin_out_w_ref.png'), [5, -15], 'FillValues', 0);
    end
    
    tmp = uint8(ones(size(seg))) - uint8(seg);
    img_bg = img.*tmp;
    img_bg = img_bg + uint8(seg).*out;
    
    img_bg(img_bg>255) = 255;
    
    mkdir(sprintf('%s/images/seq%04d', save_dir, k));
    mkdir(sprintf('%s/maps/seq%04d',   save_dir, k));
    imwrite(img,    sprintf('%s/images/seq%04d/0001.png', save_dir, k));
    imwrite(img_bg, sprintf('%s/maps/seq%04d/0001.png',   save_dir, k));
end