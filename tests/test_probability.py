from topic_selector.selection.probability import (
    normalise_probs,
    get_distr,
    clean_prios,
    # prios_to_probs,
    dash_prios_to_normalised_probs,
)
import numpy as np

prios_dash = ["", "1", "2", "5"]
probs_unnorm = [1, 2, 1]


def test_normalise_probs():
    assert np.all(normalise_probs(probs_unnorm) == np.array([0.25, 0.5, 0.25]))


def test_get_distribution():
    probs = normalise_probs(probs_unnorm)
    distribution = get_distr(probs)


def test_clean_prios():
    prios_clean = clean_prios(prios_dash)
    assert prios_clean == [3, 1, 2, 5]


# def test_prios_to_probs():
#     prios_clean = clean_prios(prios_dash)
#     # probability should be inverse
#     assert np.all(prios_to_probs(prios_clean) == np.array([1 / 3, 1, 1 / 2, 1 / 5]))


def test_dash_to_probs():
    probs = dash_prios_to_normalised_probs(prios_dash)
    assert np.all(probs == np.array([3, 1, 2, 5]) / 11)
