import random
import numpy as np


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
