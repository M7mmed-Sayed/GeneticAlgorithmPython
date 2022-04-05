import numpy
#import matplotlib.pyplot

def _fitness(inputs, population):
    # Calculating  fitness F() for each population.
    fit = numpy.sum(population*inputs, axis=1)
    return fit

def select(pop, fitness):
    # genrate matrix (3.6) for parents.
    parents = numpy.empty((3, 6))
    for p in range(3):
        mx= numpy.max(fitness)
        mxfit_array = numpy.where(fitness == mx)
        mxfit_indx = mxfit_array[0][0]
        parents[p, :] = pop[mxfit_indx, :]
        fitness[mxfit_indx] = -10000000
    return parents

def crossover(parents):
    cross = numpy.empty((3,6))
    # the centre to split parents gens.
    mid_point = 3
    for p in range(3):
        # first , second parents.
        p1 = p%3
        p2 = (p+1)%3
        #genration new gen
        cross[p, 0:mid_point] = parents[p1, 0:mid_point]
        cross[p, mid_point:] = parents[p2, mid_point:]
    return cross

def mutation(mutationgens):
    # Mutation changes the 5 gen for each genration.
    for i in range(3):
        mutationgens[i, 4] = mutationgens[i, 4] / 2.0
    return mutationgens

def best_idx(fitness):
    best_gen = numpy.where(fitness == numpy.max(fitness)) # array have max fitness  index 
    ind=best_gen[0][0]
    return ind
    
# draw graph for explanation 
#def drawgraph(best_outputs):
  #  matplotlib.pyplot.plot(best_outputs)
    #matplotlib.pyplot.xlabel("Iteration")
   # matplotlib.pyplot.ylabel("Fitness")
   # matplotlib.pyplot.show()
