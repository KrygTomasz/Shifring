import Huffman
import numpy as np

class Compression:

    def compress(self, array):

        width = len(array[0])
        print width
        array = array.flatten()
        print array
        print len(array)

        for i in range(len(array)):
            if -0.99 < array[i] < 0.99:
                array[i] = 0
            array[i] = round(array[i], 0)

        text = str(array.tolist())
        text = text.replace(' ', '')
        text = text.replace('.0', '')
        print text

        encoder = Huffman.Encoder(text)
        encoder.write('compressedFile.cgk')

    def decompress(self, fileName):
        decoder = Huffman.Decoder(fileName)
        decodedText = decoder.decode()
        print decodedText
        listed = list(eval(decodedText))
        print listed
        print len(listed)
        numpyArray = np.array(listed)
        shape = (300, 300)
        matrix = numpyArray.reshape(shape)
        print matrix.shape
        print matrix
