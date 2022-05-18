from select import select
from topic_selector.selection.topic_selection import (
    select_topic,
    select_random,
    select_prob,
)

TOPICS = ["climbing", "lute"]
PROBS = [0.2, 0.8]


def test_select_random():
    # chosen topic must be an item in the options
    assert select_topic(TOPICS, None, selection_function=select_random) in TOPICS


def test_select_prob():
    # chosen topic must be an item in the options
    assert select_topic(TOPICS, PROBS, selection_function=select_prob) in TOPICS
