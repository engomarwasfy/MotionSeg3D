#!/usr/bin/env python3
# This file is covered by the LICENSE file in the root of this project.

import os
import sys
import cv2
import numpy as np
from glob import glob


if __name__ == '__main__':

    path = "data/sequences/00/"

    save_path = os.path.join(path, "concate_residual")

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    files = sorted(glob(os.path.join(path, "velodyne/*.bin")))

    for fid in range(8, len(files)):

        for i in range(1, 9):
            tmp = f"{path}/visualization_{i}/{'%06d'%fid}.png"
            print(tmp)
            tmp_img = cv2.imread(tmp)
            img = tmp_img if i == 1 else np.concatenate((img, tmp_img), axis=0)
        cv2.imshow("residual image", img)
        cv2.waitKey()
