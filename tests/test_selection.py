from select import select
from topic_selector.selection.topic_selection import select_topic

TOPICS = ["climbing", "lute"]


def test_select_topic():
    # chosen topic must be an item in the options
    assert select_topic(TOPICS, None) in TOPICS
