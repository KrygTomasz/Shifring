import Huffman
import numpy as np

class Compression:

    def compress(self, array):
        print array
        width = len(array[0])

        array = array.flatten()
        array = np.append(array,width)
        text = "["
        for i in range(len(array)-1):
            text += str(array[i])+","
        text += str(array[len(array)-1]) + "]"
        print text
        encoder = Huffman.Encoder(text)
        encoder.write('compressedFile.cgk')

    def decompress(self, fileName):
        decoder = Huffman.Decoder(fileName)
        decodedText = decoder.decode()
        listed = list(eval(decodedText))
        width = int(listed.pop())
        height = int(len(listed)/width)
        numpyArray = np.array(listed)
        shape = (width, height)
        matrix = numpyArray.reshape(shape)
        #print matrix
        return matrix
