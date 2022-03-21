#!/usr/bin/env Python
# -*- coding: utf-8 -*-

"""
@author: 陈 子坤 (GitHub@sandyzikun)
@time: 2022-03-19 18:39
"""

import numpy as np, cv2
from matplotlib import pyplot as plt
plt.style.use("solarized-light")

class Constants(object):
    PATH_IMAGE = "./meteor.jpeg"

if __name__ == "__main__":
    plt.rcParams["figure.figsize"] = (12, 4)
    #plt.rcParams["figure.facecolor"] = "#fdf6e3"
    img_arr = cv2.imread(Constants.PATH_IMAGE)
    img_height, img_width, _ = img_arr.shape
    # Image Zooming-out / 图像缩小
    """
    cv2.imshow(
        "Image Zooming-out",
        cv2.resize(
            img_arr,
            (img_width // 2, img_height // 2),
            interpolation=cv2.INTER_CUBIC # Using Cubic Interpolation / 使用二次曲线插值
            )
        )
    cv2.waitKey()
    """
    plt.subplot(121)
    plt.title("Image Origin")
    plt.imshow(img_arr[ : , : , : : (-1) ])
    plt.subplot(122)
    plt.title("Image Zooming-out")
    plt.imshow(
        cv2.resize(
            img_arr,
            (img_width // 2, img_height // 2),
            interpolation=cv2.INTER_CUBIC # Using Cubic Interpolation / 使用二次曲线插值
            )[ : , : , : : (-1) ]
        )
    plt.savefig("./fig-01.jpeg")
    plt.show()
    plt.clf()
    # Image Zooming-in / 图像放大
    plt.subplot(121)
    plt.title("Image Origin")
    plt.imshow(img_arr[ : , : , : : (-1) ])
    plt.subplot(122)
    plt.title("Image Zooming-in")
    plt.imshow(
        cv2.resize(
            img_arr,
            (img_width * 2, img_height * 2),
            interpolation=cv2.INTER_LINEAR # Using Linear Interpolation / 使用线性插值
            )[ : , : , : : (-1) ]
        )
    plt.savefig("./fig-02.jpeg")
    plt.show()
    plt.clf()
    # Image Shifting / 图像平移
    plt.subplot(121)
    plt.title("Image Origin")
    plt.imshow(img_arr[ : , : , : : (-1) ])
    plt.subplot(122)
    plt.title("Image Shifted")
    plt.imshow(
        cv2.warpAffine(
            img_arr,
            np.float32([ # Transformation (Shifting) Matrix (shape: 2x3)
                [ 1 , 0 , -164 ],
                [ 0 , 1 , -128 ],
                ]),
            (img_width, img_height)
            )[ : , : , : : (-1) ]
        )
    plt.savefig("./fig-03.jpeg")
    plt.show()
    plt.clf()
    # Image Rotation / 图像旋转
    plt.subplot(121)
    plt.title("Image Origin")
    plt.imshow(img_arr[ : , : , : : (-1) ])
    plt.subplot(122)
    plt.title("Image Rotated")
    plt.imshow(
        cv2.warpAffine(
            img_arr,
            cv2.getRotationMatrix2D(
                (round(img_width / 2), round(img_height / 2)),
                39,
                1.28
                ),
            (img_width, img_height)
            )[ : , : , : : (-1) ]
        )
    plt.savefig("./fig-04.jpeg")
    plt.show()
    plt.clf()
    # Affine Transformation / 仿射变换
    plt.subplot(121)
    plt.title("Image Origin")
    plt.imshow(img_arr[ : , : , : : (-1) ])
    plt.subplot(122)
    plt.title("Image Affine-transformed")
    plt.imshow(
        cv2.warpAffine(
            img_arr,
            cv2.getAffineTransform(
                np.float32([
                    [  50 ,  50 ],
                    [ 200 ,  50 ],
                    [  50 , 200 ],
                    ]),
                np.float32([
                    [  10 , 100 ],
                    [ 200 ,  20 ],
                    [ 100 , 250 ],
                    ])
                ),
            (img_width, img_height)
            )[ : , : , : : (-1) ]
        )
    plt.savefig("./fig-05.jpeg")
    plt.show()
    plt.clf()
