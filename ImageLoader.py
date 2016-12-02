import numpy as np

from PIL import Image

class ImageLoader:

    def __init__(self, imagePath):
        self.image = Image.open(imagePath)

    def getImage(self):
        return self.image

    def getRedChannel(self):
        redChannel = self.image.split()[0].convert("L")
        return redChannel

    def getGreenChannel(self):
        greenChannel = self.image.split()[1].convert("L")
        return greenChannel

    def getBlueChannel(self):
        blueChannel = self.image.split()[2].convert("L")
        return blueChannel

    def getGrayLevel(self):
        redChannel = self.image.convert("L")
        return redChannel

    def mergeChannelsToImg(self,redChannel,greenChannel,blueChannel):
        width = redChannel[0].size
        height = redChannel.size/width
        channels = 3
        img = np.zeros((height, width, channels), dtype=np.uint8)
        for y in range(img.shape[0]):
            for x in range(img.shape[1]):
                r, g, b = (redChannel[y][x],greenChannel[y][x],blueChannel[y][x])
                img[y][x][0] = self.boundValue(r)
                img[y][x][1] = self.boundValue(g)
                img[y][x][2] = self.boundValue(b)

        return img

    def boundValue(self,value):
        if(value>254):
           return 255
        else:
            if (value < 0):
                return 0
            else:
                return value