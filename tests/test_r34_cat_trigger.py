import pytest
from triggers.r34_cat_trigger import R34CatTrigger

trigger = R34CatTrigger()

class DummyMessage:
    def __init__(self, content):
        self.content = content
        self.mentions = []

def test_exact_match(): 
    msg = DummyMessage("hfsdklar34fsda  lkh.1/.2f")
    assert trigger.match(msg) is True

def test_variant_match():
    msg = DummyMessage("fhsafR34sdahf  1324[];;';'")
    assert trigger.match(msg) is True

def test_no_match():
    msg = DummyMessage("nothing suspicious here")
    assert trigger.match(msg) is False
