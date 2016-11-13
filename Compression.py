import Huffman


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
        f = open('encrypted.txt', 'w')
        f.write(huffman.encode(text))
        f.close()
