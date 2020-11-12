import numpy

def task1_1(equation_inputs, pop):
    fitness = numpy.sum(pop * equation_inputs, axis=1)
    return fitness