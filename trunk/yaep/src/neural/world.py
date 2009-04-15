'''
Created on Apr 14, 2009

@author: HP_Administrator
'''


import psyco
psyco.full()

import tester
import neuralNet
import numpy
import random 
import profile

class breeder:
    
    def breed(self, population):
        A = numpy.array([population[i].feature() for i in range(1, len(population))])
        U, s, Vh = numpy.linalg.svd(A)
        return population

class selector:
    
    def select(self, weightedPop):
        def add(acc, smple):
            weight = smple[0]
            return weight + acc
        weightsum = reduce(add, weightedPop, 0)
        print('avg:', (weightsum / len(weightedPop)))
        rndnumbers = [(random.random() * weightsum) for i in range(0, len(weightedPop))]
        def selectone(seed):
            accum = 0
            for i in range(0, len(weightedPop)):
                accum += weightsum - weightedPop[i][0]
                if accum > seed:
                    break
            return weightedPop[i][1]
        return map(selectone,rndnumbers)
    
class mutator:
    def mutate(self, pop):
        def mutatesingle(nn):
            nn.weights += numpy.random.rand(nn.states, nn.states) * 2 - 1
            return nn
        return map(mutatesingle,pop)

class environment:
    tester = tester.tester()
    def eval(self,nn):
        result = self.tester.testWithString(nn, 'This is a test sequence test sequence')
        return result
        
        
class reporter:
    environment = environment()
    def report(self, pop):
        print('---')
        #print(map(self.environment.eval,pop))


class world:
    environment = environment()
    selector = selector()
    population = []
    breeder = breeder()
    mutator = mutator()
    reporter = reporter()
    size = 500
    inds = 5
    
    def step(self):
        def mapFunc(x):
             return [self.environment.eval(x), x]
        weightedPop = numpy.array([mapFunc(self.population[i]) for i in range(0,self.inds)])
        newPop = self.selector.select(weightedPop)
        newPop = self.mutator.mutate(newPop)
        newPop = self.breeder.breed(newPop)
        self.reporter.report(newPop)
        
    
    def run(self):
        while 1 == 1:
            self.step()

    def __init__(self):
        self.population = numpy.array([neuralNet.neuralnet(self.size) for i in range(self.inds)])
        '''
        Constructor
        '''

def main():
    myWorld = world()
    myWorld.run()

#if __name__ == '__main__':
#profile.run('main()')
main()

        