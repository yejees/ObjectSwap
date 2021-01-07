clear; close all; clc;

file_name = 'vitamin.png';
load_dir = 'bottle_vitamin_samples';

img = imresize(imread(sprintf('%s/%s', load_dir, file_name)), [1440 1440]);

figure; imshow(img);
[x,y] = getpts;

x = round(x);
y = round(y);

imwrite(img, sprintf('%s/%s.jpg', load_dir, file_name(1:end-4)));
save(sprintf('%s/%s_lm.mat', load_dir, file_name(1:end-4)), 'x', 'y');