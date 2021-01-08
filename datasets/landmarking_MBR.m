clear; close all; clc;

obj = 'mbn_bottle2';

load_dir = sprintf('%s_seg_no_occ_85', obj);

save_dir = sprintf('%s_lm_MBR_no_occ_85', obj);
if exist(save_dir, 'dir')
    rmdir(save_dir, 's');
end
mkdir(save_dir);

filepath = dir(fullfile(load_dir, '*.png'));

% for i = 1
for i = 1 : length(filepath)
    fprintf(sprintf('%d/%d\n', i, length(filepath)));
    file_name = filepath(i).name;
    img = imread(sprintf('%s/%s', load_dir, file_name));
    [nx, ny] = size(img);
    [indy, indx] = find(img);

    X = permute(cat(2, indx, indy), [2, 1]);
    c = round(minBoundingBox(X));
    
    if i >= 129 && i <= 150
        c = c(:,[4,3,2,1]);       
    elseif i >= 151 && i <= 165
        c = c(:,[3,2,1,4]);
    elseif i >= 166 && i <= 186
        c = c(:,[4,3,2,1]);
    elseif i >= 383 && i <= 416
        c = c(:,[4,3,2,1]);
    else
        c = c(:, [1,4,3,2]);
    end
    
    c(c<1)  = 1;
    c(c>nx) = nx;
    
    x = c(1,:);
    x = x(:);    
    y = c(2,:);
    y = y(:);
    
    save(sprintf('%s/%s_lm.mat', save_dir, file_name(1:end-6)), 'x', 'y');
end

figure(1);
hold off, plot(X(1,:), X(2,:), '.'); xlim([1 512]); ylim([1 512]);
hold on,  plot(c(1,[1:end 1]), c(2,[1:end 1]), 'r')
axis equal