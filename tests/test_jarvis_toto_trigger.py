import pytest
from triggers.jarvis_toto_trigger import JarvisTotoTrigger

trigger = JarvisTotoTrigger()

class DummyMessage:
    def __init__(self, content, mentions=None):
        self.content = content
        self.mentions = mentions or []

def test_trigger_with_jarvis_and_mention():
    msg = DummyMessage("Hey jarvis @user", mentions=["user"])
    assert trigger.match(msg) is True

def test_no_trigger_without_jarvis():
    msg = DummyMessage("Hey @user", mentions=["user"])
    assert trigger.match(msg) is False

def test_no_trigger_without_mention():
    msg = DummyMessage("Hey jarvis", mentions=[])
    assert trigger.match(msg) is False

def test_trigger_case_insensitive():
    msg = DummyMessage("Jarvis @user", mentions=["user"])
    assert trigger.match(msg) is True

def test_trigger_with_multiple_mentions():
    msg = DummyMessage("jarvis @user1 @user2", mentions=["user1", "user2"])
    assert trigger.match(msg) is True

def test_trigger_with_jarvis_in_word():
    msg = DummyMessage("ajarvis @user", mentions=["user"])
    assert trigger.match(msg) is True

def test_trigger_when_jarvis_and_mention_without_space():
    msg = DummyMessage("jarvis@user", mentions=["user"])
    assert trigger.match(msg) is True
