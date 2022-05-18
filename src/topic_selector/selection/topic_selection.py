"""Functions for choosing topics"""

import random
import numpy as np
from topic_selector.selection.probability import get_distr


def select_random(topics, probs=None, set_seed=False):
    """Randomly select a topic

    Parameters
    ----------
    topics : iterable of str
        Topics to select
    probs : iterable of float, optional
        Probability of selecting each topic, by default None

    Returns
    -------
    str
        selected topic
    """
    if set_seed:
        random.seed(42)
    return random.choice(topics)


def select_prob(topics, probs, set_seed=False):
    distr = get_distr(probs)
    idx = distr.rvs(size=1, random_state=42 if set_seed else None)
    return topics[idx[0]]


def select_topic(topics, probs=None, selection_function=select_random, *args, **kwargs):
    """Select a topic

    Parameters
    ----------
    topics : iterable of str
        Topics to select
    probs : iterable of float
        Probability of selecting each topic, by default None
    selection_function: function, optional
        Function to use when selecting topic

    Returns
    -------
    str
        selected topic
    """
    return selection_function(topics, probs, *args, **kwargs)
