clear; close all; clc;

obj_name1 = 'bottle';
obj_name2 = 'vitamin';

load_dir1 = sprintf('%s_seg',  obj_name1);
load_dir2 = sprintf('%s_seg',  obj_name2);

save_dir = sprintf('../pytorch-CycleGAN-and-pix2pix/datasets/%s2%s_m2m', obj_name1, obj_name2);

if exist(save_dir, 'dir')
    rmdir(save_dir, 's');
end

mkdir(sprintf('%s/trainA', save_dir));
mkdir(sprintf('%s/testA',  save_dir));
mkdir(sprintf('%s/trainB', save_dir));
mkdir(sprintf('%s/testB',  save_dir));

file_list1 = dir(fullfile(load_dir1, '*.png'));
file_list2 = dir(fullfile(load_dir2, '*.png'));

num_data1 = length(file_list1);
num_data2 = length(file_list2);
% num_train = round(0.85 * num_data);
% num_val   = round(0.05 * num_data);
% num_test  = num_data - num_train - num_val;

ind_list1 = randperm(num_data1);
ind_list2 = randperm(num_data2);

file_list1 = file_list1(ind_list1);
file_list2 = file_list2(ind_list2);

for k = 1 : num_data1
    k
    seg  = imread(sprintf('%s/%s', load_dir1, file_list1(k).name));
        
    imwrite(seg, sprintf('%s/trainA/%04d.png',  save_dir, k));
    imwrite(seg, sprintf('%s/testA/%04d.png',   save_dir, k));
end

for k = 1 : num_data2
    k
    seg  = imread(sprintf('%s/%s', load_dir2, file_list2(k).name));
        
    imwrite(seg, sprintf('%s/trainB/%04d.png',  save_dir, k));
    imwrite(seg, sprintf('%s/testB/%04d.png',   save_dir, k));
end

