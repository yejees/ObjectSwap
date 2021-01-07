clear; close all; clc;

load_folder = 'vitamin';

load_dir = dir(fullfile(load_folder, '*.png'));

save_dir = sprintf('%s_temp', load_folder);
mkdir(save_dir);

for i = 1 : length(load_dir)
    img = im2double(uint8(imread(sprintf('%s/%s', load_folder, load_dir(i).name))));
    msk = im2double(imread(sprintf('%s_seg/%s_0.png', load_folder, load_dir(i).name(1:end-4))));
    
    imwrite(rgb2gray(img).*msk, sprintf('%s/%s', save_dir, load_dir(i).name));
end