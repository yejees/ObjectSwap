clear; close all; clc;

file_name = 'vitamin_seg.jpg';
load_dir = 'bottle_vitamin_samples';

img = imread(sprintf('%s/%s', load_dir, file_name));

nx = size(img, 1);
[indy, indx] = find(img);

X = permute(cat(2, indx, indy), [2, 1]);
c = round(minBoundingBox(X));
c = c(:, [4,3,2,1]);

c(c<1)  = 1;
c(c>nx) = nx;

x = c(1,:);
x = x(:);    
y = c(2,:);
y = y(:);

save(sprintf('%s/%s_lm_MBR.mat', load_dir, file_name(1:end-4)), 'x', 'y');

figure(1);
hold off, plot(X(1,:), X(2,:), '.'); xlim([1 nx]); ylim([1 nx]);
hold on,  plot(c(1,[1:end 1]), c(2,[1:end 1]), 'r')
axis equal