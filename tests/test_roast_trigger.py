import pytest
from triggers.roast_trigger import RoastTrigger

trigger = RoastTrigger()

class DummyMessage:
    def __init__(self, content):
        self.content = content
        self.mentions = []

def test_exact_match():
    msg = DummyMessage("shakal dekh")
    assert trigger.match(msg) is True

def test_no_match():
    msg = DummyMessage("nothing suspicious here")
    assert trigger.match(msg) is False