import pywt


class WaveletTransform:

    def __init__(self, methodName,threshold):
        self.method = methodName
        self.threshold = threshold

    def tranrform(self, image):
        coeffs2 = pywt.dwt2(image, 'haar')
        LL, (LH, HL, HH) = coeffs2
        self.lossyCompress(LH, self.threshold)
        self.lossyCompress(HL, self.threshold)
        self.lossyCompress(HH, self.threshold)
        return [LL, LH, HL]

    def reconstruct(self, coeffs):
        HH = self.lossyCompress(coeffs[1],256)
        coeffs2 = coeffs[0], (coeffs[1], coeffs[2], HH)
        return pywt.idwt2(coeffs2, 'haar')

    def lossyCompress(self,dataArray,threshold):
        width = len(dataArray[0])
        #height = dataArray.size / width
        height = len(dataArray[0])
        for y in range(width):
            for x in range(height):
                if(dataArray[y][x]<threshold and dataArray[y][x]>-threshold):
                    dataArray[y][x] = 0