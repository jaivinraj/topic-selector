from scipy.stats import rv_discrete


def normalise_probs(probs):
    return probs / probs.sum()


def get_distr(probs, name="topic_distr"):
    return rv_discrete(name=name, values=(range(len(probs)), probs))
