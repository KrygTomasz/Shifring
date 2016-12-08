#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

import pywt.data
from PIL import Image

import Compression

from ImageLoader import ImageLoader
from WaveletTransform import WaveletTransform

waveletTransform = WaveletTransform('haar',40)

picture = "picture21.bmp"

image = ImageLoader("SampleImages/"+picture)


plotImg = plt.figure()
plt.imshow(image.getImage(), interpolation="nearest", cmap=plt.cm.gray)
plt.title("Input image", fontsize=12)
plt.show()


redImg = image.getRedChannel()
greenImg = image.getGreenChannel()
blueImg = image.getBlueChannel()

plotImg = plt.figure()

titles = ['Red Channel','Green Channel','Blue Channel']
for i, a in enumerate([redImg,greenImg,blueImg]):
    ax = plotImg.add_subplot(2, 2, i + 1)
    ax.imshow(a, interpolation="nearest", cmap=plt.cm.gray)
    ax.set_title(titles[i], fontsize=12)
plt.show()


coefsRed = waveletTransform.tranrform(redImg)
coefsGreen = waveletTransform.tranrform(greenImg)
coefsBlue = waveletTransform.tranrform(blueImg)


plotImg = plt.figure()
titles = ['Approximation', ' Horizontal detail',
          'Vertical detail', 'Diagonal detail']
for i, a in enumerate(coefsRed):
    ax = plotImg.add_subplot(2, 2, i + 1)
    ax.imshow(a, interpolation="nearest", cmap=plt.cm.gray)
    ax.set_title(titles[i], fontsize=12)
plt.show()


reconstructedRed = waveletTransform.reconstruct(coefsRed)
reconstructedGreen = waveletTransform.reconstruct(coefsGreen)
reconstructedBlue = waveletTransform.reconstruct(coefsBlue)

reconstructedImg = image.mergeChannelsToImg(reconstructedRed,reconstructedGreen,reconstructedBlue)

plotImg = plt.figure()
ax = plotImg.add_subplot(1, 2,  1)
ax.imshow(image.getImage(), interpolation="nearest", cmap=plt.cm.gray)
ax.set_title("Original", fontsize=12)

ax = plotImg.add_subplot(1, 2, 2)
ax.imshow(reconstructedImg, interpolation="nearest", cmap=plt.cm.gray)
ax.set_title("Reconstructed", fontsize=12)
plt.show()

# Load image
#original = pywt.data.aero()
#original = Image.open("picture2.jpg").convert('L')


'''
# Wavelet transform of image, and plot approximation and details
titles = ['Approximation', ' Horizontal detail',
          'Vertical detail', 'Diagonal detail']
coeffs2 = pywt.dwt2(original, 'haar')
LL, (LH, HL, HH) = coeffs2
fig = plt.figure()
for i, a in enumerate([LL, LH, HL, HH]):
    ax = fig.add_subplot(2, 2, i + 1)
    ax.imshow(a, origin='image', interpolation="nearest", cmap=plt.cm.gray)
    ax.set_title(titles[i], fontsize=12)
print("Coefs:")
print(coeffs2)
print("///////////////")

fig.suptitle("dwt2 coefficients", fontsize=14)

# Now reconstruct and plot the original image
reconstructed = pywt.idwt2(coeffs2, 'haar')
fig = plt.figure()
plt.imshow(reconstructed, interpolation="nearest", cmap=plt.cm.gray)

# Check that reconstructed image is close to the original
np.testing.assert_allclose(original, reconstructed, atol=1e-13, rtol=1e-13)

plt.show()

compression = Compression.Compression()
compression.compress(LL)

fileName = 'compressedFile.cgk'

decompress = compression.decompress(fileName)


fig = plt.figure()
plt.imshow(decompress, interpolation="nearest", cmap=plt.cm.gray)

plt.show()

'''