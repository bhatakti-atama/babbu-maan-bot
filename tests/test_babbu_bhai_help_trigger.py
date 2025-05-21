import pytest
from triggers.babbu_bhai_help_trigger import BabbuBhaiHelpTrigger

trigger = BabbuBhaiHelpTrigger()

class DummyMessage:
    def __init__(self, content):
        self.content = content
        self.mentions = []

def test_exact_match(): 
    msg = DummyMessage("babbu bhai help")
    assert trigger.match(msg) is True

def test_no_match():
    msg = DummyMessage("nothing suspicious here")
    assert trigger.match(msg) is False
