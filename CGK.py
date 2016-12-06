from Huffman import Encoder, Decoder
from ImageLoader import ImageLoader
from WaveletTransform import WaveletTransform
from RLE import RLE
import simplejson as json
import numpy as np

class CGK:

    def compressImage(self,imgPath,threshold):
        waveletTransform = WaveletTransform('haar')
        image = ImageLoader(imgPath)

        redImg = image.getRedChannel()
        greenImg = image.getGreenChannel()
        blueImg = image.getBlueChannel()

        coefsRed = waveletTransform.tranrform(redImg)
        coefsGreen = waveletTransform.tranrform(greenImg)
        coefsBlue = waveletTransform.tranrform(blueImg)
        coefs = [coefsRed, coefsGreen, coefsBlue]

        coefsStr = self.coefsToStr(coefs)
        coefsStr = RLE.Encode(coefsStr)
        #print coefsStr
        encoder = Encoder(coefsStr)
        encoder.write('compressedFile.cgk')
        '''
        text_file = open("RLE.txt", "w")
        text_file.write(coefsStr)
        text_file.close()
        '''
        return coefsStr

    def decompressImage(self, filePath,stra):
        waveletTransform = WaveletTransform('haar')

        decoder = Decoder('compressedFile.cgk')
        str = decoder.decode()
        str = RLE.Decode(str)

        coefs = self.strToCoefs(str)
        imageRed = waveletTransform.reconstruct(coefs[0])
        imageGreen = waveletTransform.reconstruct(coefs[1])
        imageBlue = waveletTransform.reconstruct(coefs[2])
        reconstructedImage = ImageLoader.mergeChannelsToImg(imageRed,imageGreen,imageBlue)
        return reconstructedImage

    def coefsToStr(self,coefs):
        list = np.array(coefs).tolist()
        for channelCoefs in list:
            for coefs in channelCoefs:
                for array in coefs:
                    for value in array:
                        value
        list = [ [[['%.0f' % value for value in array] for array in coefs] for coefs in channelCoefs] for channelCoefs in list ]

        coefsStr = json.dumps(list)
        coefsStr = coefsStr.replace("\"", "")
        coefsStr = coefsStr.replace(" ", "")

        return coefsStr

    def strToCoefs(self, str):
        coefs = json.loads(str)
        return coefs