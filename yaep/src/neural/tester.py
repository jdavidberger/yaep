'''
Created on Apr 14, 2009

@author: HP_Administrator
'''
import numpy
import math

class tester:
    corpus = ""

    def makeInput(self, symbol):
        input = numpy.zeros(60)
        input[ord(symbol) - 65] = 1.0
        return input
        
    def testWithString(self, nn, corpus):
        rtn = 0
        while len(corpus) > 0:   
            symbol = corpus[0]
            input = self.makeInput(symbol)
            expected = self.makeInput(corpus[0])
            diff, ran = nn.runWithInputs(input, expected, 10)
            rtn += diff
            corpus = corpus[1:]
       # print(expected)
       # print(nn.state[-60:])
        print(rtn)
        return rtn
     
        
    def __init__(self):
        '''
        Constructor
        '''

        
if __name__ == '__main__':
    t = tester()
    t.makeInput('a')
        