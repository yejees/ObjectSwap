clear; close all; clc;

file_name = '0417.png';

load_dir = 'mbn_bottle2';
save_dir = sprintf('%s_lm', load_dir);

% if exist(save_dir, 'dir')
%     rmdir(save_dir, 's');
% end
mkdir(save_dir);

img = imread(sprintf('%s/%s', load_dir, file_name));

figure; imshow(img);
[x,y] = getpts;

x = round(x);
y = round(y);

save(sprintf('%s/%s_lm.mat', save_dir, file_name(1:end-4)), 'x', 'y');