from numpy import asarray
from numpy import arange
from numpy.random import randn
from numpy.random import rand
from numpy.random import seed
from matplotlib import pyplot

def myfunc(x):
    return x[0] ** 2.0

# hill climbing local search algorithm
def hillclimbing(myfunc, bounds, n_iterations, step_size):

    sol = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
    solution_eval = myfunc(sol)
    solutions = list()
    solutions.append(sol)
    for i in range(n_iterations):

      candidate = sol + randn(len(bounds)) * step_size
      candidte_eval = myfunc(candidate)
    # check if we should keep the new point
      if candidte_eval <= solution_eval:
    # store the new point
        sol, solution_eval = candidate, candidte_eval
    # keep track of solutions
        solutions.append(sol)
    # report progress
    print('>%d f(%s) = %.5f' % (i, sol, solution_eval))
    return [sol, solution_eval, solutions]


# seed the pseudorandom number generator
seed(5)
# define range for input
bounds = asarray([[-5.0, 5.0]])
# define the total iterations
n_iterations = 2000
# define the maximum step size
step_size = 0.1
# perform the hill climbing search
best, score, solutions = hillclimbing(myfunc, bounds, n_iterations, step_size)
print('Compelete!')
print('f(%s) = %f' % (best, score))
# sample input range uniformly at 0.1 increments
inputs = arange(bounds[0, 0], bounds[0, 1], 0.1)
# create a line plot of input vs result
pyplot.plot(inputs, [myfunc([x]) for x in inputs], '--')
# draw a vertical line at the optimal input
pyplot.axvline(x=[0.0], ls='--', color='pink')

pyplot.plot(solutions, [myfunc(x) for x in solutions], 'o', color='silver')
pyplot.show()
