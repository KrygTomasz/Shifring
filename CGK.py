from Huffman import Encoder, Decoder
from ImageLoader import ImageLoader
from WaveletTransform import WaveletTransform
from RLE import RLE
import simplejson as json
import numpy as np

class CGK:

    def compressImage(self,imgPath,threshold,RLEspan):
        self.threshold = threshold
        waveletTransform = WaveletTransform('haar',self.threshold)
        image = ImageLoader(imgPath)
        print "Image loaded"
        redImg = image.getRedChannel()
        greenImg = image.getGreenChannel()
        blueImg = image.getBlueChannel()
        print "Channels ready"
        coefsRed = waveletTransform.tranrform(redImg)
        coefsGreen = waveletTransform.tranrform(greenImg)
        coefsBlue = waveletTransform.tranrform(blueImg)
        coefs = [coefsRed, coefsGreen, coefsBlue]
        print len(coefsRed[0])
        print "Img transformed"

        coefsStr = self.coefsToStr(coefs)

        print "Json ready"

        coefsStr = RLE.Encode(coefsStr,RLEspan)

        print "RLEed"

        encoder = Encoder(coefsStr)
        encoder.write(imgPath + '.cgk')

        print "Compression done."

        '''
        text_file = open("RLE.txt", "w")
        text_file.write(coefsStr)
        text_file.close()
        '''
        return coefsStr

    def decompressImage(self, filePat):
        waveletTransform = WaveletTransform('haar',0)

        decoder = Decoder(filePat)
        str = decoder.decode()

        print "Huffman decoded"

        str = RLE.Decode(str)

        print "RLE decoded"

        coefs = self.strToCoefs(str)

        print "Coefs parsed"
        imageRed = waveletTransform.reconstruct(coefs[0])
        imageGreen = waveletTransform.reconstruct(coefs[1])
        imageBlue = waveletTransform.reconstruct(coefs[2])
        reconstructedImage = ImageLoader.mergeChannelsToImg(imageRed,imageGreen,imageBlue)

        print "Img reconstructed"
        return reconstructedImage

    def coefsToStr(self,coefs):
        list = np.array(coefs).tolist()
        list = [ [[['%.0f' % value for value in array] for array in coefs] for coefs in channelCoefs] for channelCoefs in list ]

        coefsRedStr = json.dumps(list[0])
        coefsRedStr = coefsRedStr.replace("\"", "")
        coefsRedStr = coefsRedStr.replace(" ", "")

        coefsGreenStr = json.dumps(list[1])
        coefsGreenStr = coefsGreenStr.replace("\"", "")
        coefsGreenStr = coefsGreenStr.replace(" ", "")

        coefsBlueStr = json.dumps(list[2])
        coefsBlueStr = coefsBlueStr.replace("\"", "")
        coefsBlueStr = coefsBlueStr.replace(" ", "")

        coefsStr = "["+coefsRedStr+","+coefsGreenStr+","+coefsBlueStr+"]";

        return coefsStr

    def strToCoefs(self, str):
        coefs = json.loads(str)
        return coefs