import pytest
from triggers.trucked_trigger import TruckedTrigger

trigger = TruckedTrigger()


class DummyUser:
    def __init__(self, display_name):
        self.display_name = display_name

class DummyMessage:
    def __init__(self, content):
        self.content = content
        self.mentions = [DummyUser("TestUser"), DummyUser("AnotherUser")]

def test_exact_match(): 
    msg = DummyMessage("truck  lkh.1/.2f")
    assert trigger.match(msg) is True

def test_no_match():
    msg = DummyMessage("nothing suspicious here")
    assert trigger.match(msg) is False