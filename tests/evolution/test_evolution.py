from pygrn.grns import ClassicGRN
from pygrn.problems import Counter
from pygrn.evolution import Evolution
from pygrn import config
import numpy as np


def test_noncacheable_counter():
    problem = Counter()
    problem.cacheable = False
    evo = Evolution(problem, lambda: ClassicGRN())
    evo.step()
    assert np.any([sp.sum_adjusted_fitness > 0.0
                   for sp in evo.population.species])
    assert problem.count == config.POPULATION_SIZE
    evo.step()
    assert np.any([sp.sum_adjusted_fitness > 0.0
                   for sp in evo.population.species])
    assert problem.count == 2 * config.POPULATION_SIZE
    evo.step()
    assert np.any([sp.sum_adjusted_fitness > 0.0
                   for sp in evo.population.species])
    assert problem.count == 3 * config.POPULATION_SIZE


def test_cacheable_counter():
    problem = Counter()
    problem.cacheable = True
    evo = Evolution(problem, lambda: ClassicGRN())
    evo.step()
    assert np.any([sp.sum_adjusted_fitness > 0.0
                   for sp in evo.population.species])
    assert problem.count == config.POPULATION_SIZE
    evo.step()
    assert np.any([sp.sum_adjusted_fitness > 0.0
                   for sp in evo.population.species])
    assert problem.count < 2 * config.POPULATION_SIZE
    evo.step()
    assert np.any([sp.sum_adjusted_fitness > 0.0
                   for sp in evo.population.species])
    assert problem.count < 3 * config.POPULATION_SIZE


def test_fit_increase():
    problem = Counter()
    problem.cacheable = True
    evo = Evolution(problem, lambda: ClassicGRN())
    evo.step()
    assert np.any([sp.sum_adjusted_fitness > 0.0
                   for sp in evo.population.species])
    best_fit, best_ind = evo.population.get_best()
    evo.run(10)
    new_best_fit, new_best_ind = evo.population.get_best()
    assert np.any([sp.sum_adjusted_fitness > 0.0
                   for sp in evo.population.species])
    assert new_best_fit >= best_fit
