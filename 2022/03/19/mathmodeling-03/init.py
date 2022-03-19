#!/usr/bin/env Python
# -*- coding: utf-8 -*-

"""
@author: 陈 子坤 (GitHub@sandyzikun)
@time: 2022-03-19 18:39
"""

import numpy as np, cv2

class Constants(object):
    PATH_IMAGES = [
        "./meteor.jpeg",
        ]
    TRANS_MAT_2x3 = [ # Transformation Matrix (shape: 2x3)
        ]

if __name__ == "__main__":
    img_arr = cv2.imread(Constants.PATH_IMAGES[0])
    img_height, img_width, _ = img_arr.shape
    # Zooming Image Out / 缩小图像
    cv2.imshow(
        "Zooming Image Out",
        cv2.resize(
            img_arr,
            (img_width // 2, img_height // 2),
            interpolation=cv2.INTER_CUBIC # Using Cubic Interpolation / 使用二次曲线插值
            )
        )
    cv2.waitKey()
    # Zooming Image In / 放大图像
    cv2.imshow(
        "Zooming Image In",
        cv2.resize(
            img_arr,
            (img_width * 2, img_height * 2),
            interpolation=cv2.INTER_LINEAR # Using Linear Interpolation / 使用线性插值
            )
        )
    cv2.waitKey()
    #
    # 补刀, 关闭所有创建的窗口
    cv2.destroyAllWindows()
