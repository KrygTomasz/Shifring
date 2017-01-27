#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk
import tkFileDialog as dialog
import tkMessageBox
from tkinter import Image as ImageTk
import scipy.misc

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from CGK import CGK
from ImageLoader import ImageLoader
from PIL import Image, ImageTk


def encrypt():
    print 'en'

    cgkFile = dialog.askopenfile(parent = root, initialdir='/Users/kryguu/PycharmProjects/Shifring',
                                 title='Select .bmp file', filetypes=[('.bmp files', '.bmp')])

    cgk = CGK()
    cgk.compressImage(cgkFile.name, 40, 20)

    tkMessageBox.showinfo("Information", "Image successfully encrypted.")



def decrypt():
    print 'de'

    cgkFile = dialog.askopenfile(parent = root,initialdir='/Users/kryguu/PycharmProjects/Shifring',title='Select .cgk file', filetypes=[('.cgk files', '.cgk')])

    cgk = CGK()
    reconstructedImage = cgk.decompressImage(cgkFile.name)

    scipy.misc.imsave(cgkFile.name + '.jpg', reconstructedImage)

    image = Image.open(cgkFile.name + '.jpg')
    photo = ImageTk.PhotoImage(image)

    global imageLabel
    imageLabel.config(image = photo)
    imageLabel.image = photo



root = tk.Tk()

Label1 = tk.Label(root, text = 'Welcome to amazing image encryptor and decryptor!')
Label2 = tk.Label(root, text = 'Choose what to do by clicking a button below...')
Button1 = tk.Button(root, text = 'Encrypt an image...', command = encrypt)
Button2 = tk.Button(root, text = 'Decrypt a .cgk file...', command = decrypt)
imageLabel = tk.Label(root, text = '')


Label1.pack()
Label2.pack()
Button1.pack()
Button2.pack()
imageLabel.pack()

root.mainloop()



