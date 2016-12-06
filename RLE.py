

class RLE:

    @staticmethod
    def Encode(Str):
        span = 20

        inputStr = Str
        outputStr = ""
        bufor = ""
        count = 0
        for index in range(0,len(inputStr)+span,span):
            if(inputStr[index:index+span]==bufor):
                count+=1
            else:
                outputStr += "{"+bufor+"}"+str(count)
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
            strCount = pair.split("}")
            for i in range(int(strCount[1])):
                output += strCount[0]

        return output



#print RLE.Encode("[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]")