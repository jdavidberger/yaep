'''
Created on Apr 14, 2009

@author: HP_Administrator
'''

import numpy
import math

def stepFunc(n,v):
    if (v > 0):
        return 1
    else:
        return 0

def sigmoid(n,v):
    return math.tanh(v);

class neuralnet:
    layers = []
    weights = []
    layout = []
    state = 0
    weights = 0
    phi = sigmoid
    
    def __init__(self, layout):
        self.layout = layout
        
        self.weights = numpy.random.rand(states , states) * 2 - 1
        self.state = numpy.zeros(states)
    
    def __init__(self, states):
        self.states = states
        self.weights = numpy.random.rand(states , states) * 2 - 1
        self.state = numpy.zeros(states)

    def iterate(self):
        self.state[0] = 1
        x_pre = numpy.dot(self.weights,numpy.ma.transpose(self.state))
        
        self.state = numpy.array([self.phi(x_pre[i]) for i in range(0, self.states)])

    def iterateWithInputs(self, inputs):
        self.state[0] = 1
        for i in range(0, len(inputs)):
            self.state[i + 1] = inputs[i];
        self.iterate()
        
    def run(self, length):
        return self.runWithInputs([], length)
     
    def runWithInputs(self, inputs, outputs, length):
        self.state = numpy.zeros(self.states)
        for i in range(0, length):
            self.iterateWithInputs(inputs)
            if(not any(self.state[1:])):
                break
        return 1 / numpy.linalg.norm([a - b for a, b in zip(outputs, self.state[-len(outputs):])]), i
        
if __name__ == '__main__':
    nn = neuralnet(10)
    a = nn.runWithInputs([0,1],[1, 1], 10)
    print(a)
    
            