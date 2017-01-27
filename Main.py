#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk
import tkFileDialog as dialog
import tkMessageBox
from tkinter import Image as ImageTk
import scipy.misc
import os

from CGK import CGK
from PIL import Image, ImageTk


def encrypt():
    cgkFile = dialog.askopenfile(parent = root, initialdir = currentDirectory, title = 'Select .bmp file', filetypes = [('.bmp files', '.bmp')])

    cgk = CGK()
    global threshold
    try:
        thresholdNumber = int(threshold.get())
    except Exception:
        thresholdNumber = 40
    cgk.compressImage(cgkFile.name, thresholdNumber, 20)

    tkMessageBox.showinfo("Information", "Image successfully compressed.")

def decrypt():
    cgkFile = dialog.askopenfile(parent = root,initialdir = currentDirectory,title = 'Select .cgk file', filetypes = [('.cgk files', '.cgk')])

    cgk = CGK()
    reconstructedImage = cgk.decompressImage(cgkFile.name)

    fileName = os.path.splitext(cgkFile.name)[0] + '-decompressed' + '.bmp'

    scipy.misc.imsave(fileName, reconstructedImage)

    image = Image.open(fileName)
    photo = ImageTk.PhotoImage(image)

    global imageLabel
    imageLabel.config(image = photo)
    imageLabel.image = photo

def createDialog():

    greetingLabel = tk.Label(root, text = 'Welcome to amazing image compressor and decompressor!')
    infoLabel = tk.Label(root, text = 'Choose what to do by clicking a button below...')
    compressButton = tk.Button(root, text = 'Compress an image...', command = encrypt)
    thresholdLabel = tk.Label(root, text = 'Enter threshold (higher value means higher compression):')
    global thresholdField
    thresholdField = tk.Entry(root)
    spaceLabel = tk.Label(root, text = '')
    decompressButton = tk.Button(root, text = 'Decompress a .cgk file...', command = decrypt)
    global imageLabel
    imageLabel = tk.Label(root, text = '')

    greetingLabel.pack()
    infoLabel.pack()
    compressButton.pack()
    thresholdLabel.pack()
    thresholdField.pack()
    global threshold
    thresholdField.config(textvariable = threshold)
    spaceLabel.pack()
    decompressButton.pack()
    imageLabel.pack()

currentDirectory = os.path.dirname(os.path.realpath(__file__))

root = tk.Tk()
threshold = tk.StringVar()
imageLabel = tk.Label(root, text = '')
createDialog()
root.mainloop()



