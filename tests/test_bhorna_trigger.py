import pytest
from triggers.bhorna_trigger import BhornaTrigger

trigger = BhornaTrigger()

class DummyMessage:
    def __init__(self, content):
        self.content = content
        self.mentions = []

def test_message_leght_greater_than_50():
    dummy_content = "x" * 201
    msg = DummyMessage(dummy_content)
    assert trigger.match(msg) is True
    
def test_message_leght_less_than_equal_to_50():
    dummy_content = "x" * 200
    msg = DummyMessage(dummy_content)
    assert trigger.match(msg) is False
