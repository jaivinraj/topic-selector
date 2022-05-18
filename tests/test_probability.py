from topic_selector.selection.probability import normalise_probs, get_distr
import numpy as np

probs_unnorm = np.array([1, 2, 1])


def test_normalise_probs():
    assert np.all(normalise_probs(probs_unnorm) == np.array([0.25, 0.5, 0.25]))


def test_get_distribution():
    probs = normalise_probs(probs_unnorm)
    distribution = get_distr(probs)
