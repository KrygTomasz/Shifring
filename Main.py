#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from CGK import CGK
from ImageLoader import ImageLoader

cgk = CGK()
str = cgk.compressImage("picture4.bmp", 4)

image = ImageLoader("picture4.bmp")
#print str

reconstructedImage = cgk.decompressImage("picture3.cgk", str)

plotImg = plt.figure()
ax = plotImg.add_subplot(1, 2,  1)
ax.imshow(image.getImage(), interpolation="nearest", cmap=plt.cm.gray)
ax.set_title("Original", fontsize=12)

ax = plotImg.add_subplot(1, 2, 2)
ax.imshow(reconstructedImage, interpolation="nearest", cmap=plt.cm.gray)
ax.set_title("Reconstructed", fontsize=12)
plt.show()