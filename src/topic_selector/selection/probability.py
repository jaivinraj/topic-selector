from scipy.stats import rv_discrete
import numpy as np


def normalise_probs(probs):
    # convert to array
    if isinstance(probs, list):
        probs = np.array(probs)
    # Normalise probabilities
    return probs / probs.sum()


def get_distr(probs, name="topic_distr"):
    # Get scipy probability distribution
    return rv_discrete(name=name, values=(range(len(probs)), probs))


def clean_prios(prios):
    # clean probability strings from dash app
    assert all([i.isnumeric() or i == "" for i in prios])
    return [3 if i == "" else int(i) for i in prios]


# def prios_to_probs(prios):
#     # convert priorities into probabilities
#     # use inverse for now!
#     if isinstance(prios, list):
#         prios = np.array(prios)
#     return 1 / prios


def dash_prios_to_normalised_probs(prios):
    prios_clean = clean_prios(prios)
    # probs_unnorm = prios_to_probs(prios_clean)
    probs = normalise_probs(np.array(prios_clean))
    return probs
