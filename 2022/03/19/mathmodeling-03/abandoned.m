clc, clear
mat = imread("./meteor.jpeg");
mat1 = imwarp(mat, affine2d([ 0.5 0 0 ; 0 0.5 0 ; 0 0 1 ]));
mat2 = imwarp(mat, affine2d([ 2 0 0 ; 0 2 0 ; 0 0 1 ]));
mat3 = imwarp(mat, affine2d([ 1 0 -164 ; 0 1 -128 ; 0 0 1 ]));
mat4 = imwarp(mat, affine2d([ cosd(39), -sind(39), 0 ; sind(39), cosd(39), 0 ; 0 0 1 ]));
mat5 = imwarp(mat, affine2d([ 10 200 100 ; 100 20 250 ; 0 0 1 ]));
subplot(231), imshow(mat), subplot(232), imshow(mat1), subplot(233), imshow(mat2), subplot(234), imshow(mat3), subplot(235), imshow(mat4), subplot(236), imshow(mat5)