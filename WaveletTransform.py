import pywt


class WaveletTransform:

    def __init__(self, methodName):
        self.method = methodName

    def tranrform(self, image):
        coeffs2 = pywt.dwt2(image, 'haar')
        LL, (LH, HL, HH) = coeffs2
        threshold = 3
        self.lossyCompress(LH, threshold)
        self.lossyCompress(HL, threshold)
        self.lossyCompress(HH, threshold)
        return [LL, LH, HL, HH]

    def reconstruct(self, coeffs):
        coeffs2 = coeffs[0], (coeffs[1], coeffs[2], coeffs[3])
        return pywt.idwt2(coeffs2, 'haar')

    def lossyCompress(self,dataArray,threshold):
        width = dataArray[0].size
        height = dataArray.size / width
        for y in range(width):
            for x in range(height):
                if(dataArray[y][x]<threshold and dataArray[y][x]>-threshold):
                    #print dataArray[y][x]
                    dataArray[y][x] = 0