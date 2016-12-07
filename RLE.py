

class RLE:

    @staticmethod
    def Encode(Str,RLEspan):
        span = RLEspan

        inputStr = Str
        outputStr = ""
        bufor = ""
        count = 0
        for index in range(0,len(inputStr)+span,span):
            if(inputStr[index:index+span]==bufor):
                count+=1
            else:
                outputStr += "{"+bufor+"}"
                if( count > 1):
                    outputStr += str(count)
                bufor = ""

            if (bufor == ""):
                bufor = inputStr[index:index + span]
                count = 1
        '''
        while(len(inputStr) != 0):
            print len(inputStr)
            counter = 0
            bufor = inputStr[:2]
            while(inputStr[:2]==bufor):
                inputStr = inputStr[2:]
                counter+=1
            outputStr += "{"+bufor+"}"+str(counter)
        '''
        return outputStr

    @staticmethod
    def Decode(Str):
        output = ""
        inputTable = Str.split("{")
        inputTable = inputTable[1:]
        for pair in inputTable:
            splitedPair = pair.split("}")
            if(splitedPair[1].isdigit()):
                for i in range(int(splitedPair[1])):
                    output += splitedPair[0]
            else:
                output += splitedPair[0]

        return output


#sample = "[0,0,0,0,0,0,0,0,0,GFGERGEFFADFRGWFVDRAVSDERWFCARv0,0,0,0,0,0,1]"
#print RLE.Encode(sample)
#print RLE.Decode(RLE.Encode(sample))
#print sample == RLE.Decode(RLE.Encode(sample))