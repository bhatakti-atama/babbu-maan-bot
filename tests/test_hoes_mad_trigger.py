import pytest
from triggers.hoes_mad_trigger import HoesMadTrigger

trigger = HoesMadTrigger()

class DummyMessage:
    def __init__(self, content):
        self.content = content
        self.mentions = []

def test_exact_match():
    msg = DummyMessage("mad")
    assert trigger.match(msg) is True

def test_variant_match():
    msg = DummyMessage("angry")
    assert trigger.match(msg) is True

def test_variant_match():
    msg = DummyMessage("angrybird")
    assert trigger.match(msg) is False

def test_no_match():
    msg = DummyMessage("nothing suspicious here")
    assert trigger.match(msg) is False
