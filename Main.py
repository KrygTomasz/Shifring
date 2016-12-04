#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from CGK import CGK

cgk = CGK()
str = cgk.compressImage("picture21.bmp", 4)

print str

reconstructedImage = cgk.decompressImage("picture3.cgk",str)

plotImg = plt.figure()
plt.imshow(reconstructedImage, interpolation="nearest", cmap=plt.cm.gray)
plt.title("Input image", fontsize=12)
plt.show()