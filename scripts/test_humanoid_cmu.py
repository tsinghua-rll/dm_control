#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# File Name : test_humanoid_cmu.py
# Creation Date : 09-10-2018
# Created By : Jeasine Ma [jeasinema[at]gmail[dot]com]

import os 
import glfw
try:
    glfw.init()
except:
    pass

from dm_control import suite 
from dm_control.suite import humanoid_CMU
import numpy as np
import cv2


def main():
    env = humanoid_CMU.run()
    while True:
        # side/back/front
        img = env.physics.render(height=480, width=640, camera_id='side')
        print(img.shape)
        cv2.imwrite('1.png', cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        break

if __name__ == '__main__':
    main()
