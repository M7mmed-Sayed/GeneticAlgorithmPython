import numpy
import Helper as fun # anthor py has helper functions

# Inputs X in our Example.
inputs = [4,-2,3.5,5,-11,-4.7]
"""
******************************************************
*   the fitness for each iteration is  static        *
*   population matrix is static                      *
*   mutation is div by 2 the 5th element for rhe gen *
******************************************************
"""
# population matrix. static
pop = numpy.empty((6,6))
pop[0, :] = [2.4,  0.7, 8, -2,   5,   1.1]
pop[1, :] = [-0.4, 2.7, 5, -1,   7,   0.1]
pop[2, :] = [-1,   2,   2, -3,   2,   0.9]
pop[3, :] = [4,    7,   12, 6.1, 1.4, -4]
pop[4, :] = [3.1,  4,   0,  2.4, 4.8,  0]
pop[5, :] = [-2,   3,   -7, 6,   3,    3]

print(pop)
#it's an array is used to genrate a helper graph (extra)
graph_data = []
#iteration numper
itre = 4
for it in range(itre):
    print("iteration num : ", it+1)
    #append best result  current iteration to graph_data (optional)
    graph_data.append(numpy.max(fun._fitness(inputs,pop)))
    # The best result in the current iteration.
    
    # Select the best parents from  population.
    parents = fun.select(pop, fun._fitness(inputs, pop))
    #print(parents)

    # Generating next generation using crossover.
    _crossover = fun.crossover(parents)
    #print(_rossover)

    # apply mutation in the 5th element/chromso.. by div by 2.
    _mutation = fun.mutation(_crossover)
    #print(_mutation)
    
    # print max fitness and the gen for cur population
    ind=fun.best_idx(fun._fitness(inputs, pop))#get best first gen
    print("Best Gen : ", pop[ind, :])#print best gen array
    print("best fitness : ",graph_data[len(graph_data)-1] )
    
    # merge new population with thare parents to genrate new population for next itreration.
    pop[0:3, :] = parents
    pop[3:, :] = _mutation
    #next population
    #print("cur  population\n",pop,"\n")
    


#all iteration done Successful
print ("Done ...************....\n","best ans")
ind=fun.best_idx(fun._fitness(inputs, pop))#get best first gen
graph_data.append(numpy.max(fun._fitness(inputs,pop)))


print("Best Gen : ", pop[ind, :])#print best gen array 
print("Best Gen fitness : ",graph_data[len(graph_data)-1])#max fitness

#draw our graph 
#fun.drawgraph(graph_data)
