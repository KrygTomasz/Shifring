import Huffman
from bitarray import bitarray

class Compression:

    def compress(self, array):
        print array
        print len(array)

        for i in range(len(array)):
            if -0.99 < array[i] < 0.99:
                array[i] = 0
            array[i] = round(array[i], 0)

        print array
        text = str(array.tolist())
        text = text.replace(' ', '')
        print text
        text = text.replace('.0', '')
        print text



        huffman = Huffman.Huffman()
        encryptedText = huffman.encode(text)
        print len(encryptedText)
        bits = bitarray(len(encryptedText))
        bits.setall(0)
        print encryptedText
        for i in range(len(encryptedText)):
            if encryptedText[i] == '1':
                bits[i] = 1

        #print bits

        f = open('encrypted.txt', 'wb')
        f.write(bits)
        f.close()
