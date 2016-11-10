from heapq import heappush, heappop, heapify
from collections import defaultdict

class Huffman:

    def encode(self, text):
        huffmanTable = self.createEncodingTable(text)
        print "Symbol\tHuffman Code"
        for p in huffmanTable:
            print "%s\t%s" % (p[0], p[1])

        encryptedData = ""

        for letter in text:
            for pair in huffmanTable:
                if letter == pair[0]:
                    encryptedData += pair[1]

        return encryptedData

    def createEncodingTable(self, text):
        symbolsWithFrequency = defaultdict(int)
        for ch in text:
            symbolsWithFrequency[ch] += 1
        """Huffman encode the given dict mapping symbols to weights"""
        heap = [[wt, [sym, ""]] for sym, wt in symbolsWithFrequency.items()]
        heapify(heap)
        while len(heap) > 1:
            lo = heappop(heap)
            hi = heappop(heap)
            for pair in lo[1:]:
                pair[1] = '0' + pair[1]
            for pair in hi[1:]:
                pair[1] = '1' + pair[1]
            heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
        return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))