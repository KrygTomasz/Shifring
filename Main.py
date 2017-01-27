#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk
import tkFileDialog as dialog
from tkinter import Image as ImageTk
import scipy.misc

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from CGK import CGK
from ImageLoader import ImageLoader
from PIL import Image, ImageTk


def encrypt():
    print 'en'

def decrypt():
    print 'de'

    cgkFile = dialog.askopenfile(parent=root,initialdir='/Users/kryguu/PycharmProjects/Shifring',title='Select .cgk file', filetypes=[('.cgk files', '.cgk')])

    cgk = CGK()
    reconstructedImage = cgk.decompressImage(cgkFile.name)

    scipy.misc.imsave(cgkFile.name + '.jpg', reconstructedImage)

    image = Image.open(cgkFile.name + '.jpg')
    photo = ImageTk.PhotoImage(image)

    imageLabel = tk.Label(image=photo)
    imageLabel.image = photo  # keep a reference!
    imageLabel.pack()

def removeFromDialog(item):
    item.destroy()


root = tk.Tk()

global imageLabel
imageLabel = tk.Label()

Label1 = tk.Label(root, text = 'Welcome to amazing image encryptor and decryptor!')
Label2 = tk.Label(root, text = 'Choose what to do by clicking a button below...')
Button1 = tk.Button(root, text = 'Encrypt an image...', command = encrypt)
Button2 = tk.Button(root, text = 'Decrypt a .cgk file...', command = decrypt)

Label1.pack()
Label2.pack()
Button1.pack()
Button2.pack()

root.mainloop()







picture = "picture21.bmp"
cgk = CGK()
str = cgk.compressImage("SampleImages/"+picture, 40, 20)

image = ImageLoader("SampleImages/"+picture)
#print str

reconstructedImage = cgk.decompressImage("compressedFile.cgk")

plotImg = plt.figure()
originalImage = Image.open("SampleImages/"+picture)
print originalImage
ax = plotImg.add_subplot(1, 2, 1)
#plt.imshow(originalImage, interpolation="nearest", cmap=plt.cm.gray)
#ax.imshow(image.getImage(), interpolation="nearest", cmap=plt.cm.gray)
ax.set_title("Original", fontsize=12)

ax = plotImg.add_subplot(1, 2, 2)
plt.imshow(reconstructedImage, interpolation="nearest", cmap=plt.cm.gray)
#ax.imshow(reconstructedImage, interpolation="nearest", cmap=plt.cm.gray)
ax.set_title("Reconstructed", fontsize=12)
plt.show()