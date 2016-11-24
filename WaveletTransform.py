import pywt


class WaveletTransform:

    def __init__(self, method):
        self.method = method

    def tranrform(self, image):
        coeffs2 = pywt.dwt2(image, 'haar')
        LL, (LH, HL, HH) = coeffs2
        return [LL, LH, HL, HH]

    def reconstruct(self, coeffs):
        coeffs2 = coeffs[0], (coeffs[1], coeffs[2], coeffs[3])
        return pywt.idwt2(coeffs2, 'haar')