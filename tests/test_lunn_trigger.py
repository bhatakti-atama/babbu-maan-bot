import pytest
from triggers.lunn_trigger import LunnTeVajjTrigger

trigger = LunnTeVajjTrigger()

class DummyMessage:
    def __init__(self, content):
        self.content = content
        self.mentions = []

def test_exact_match():
    msg = DummyMessage("lunn te vajj")
    assert trigger.match(msg) is True

def test_variant_match():
    msg = DummyMessage("Lund te waj")
    assert trigger.match(msg) is True

def test_no_match():
    msg = DummyMessage("nothing suspicious here")
    assert trigger.match(msg) is False
