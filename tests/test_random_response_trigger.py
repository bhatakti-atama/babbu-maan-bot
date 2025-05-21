import pytest
from unittest.mock import patch
from triggers.random_response_trigger import RandomResponseTrigger

trigger = RandomResponseTrigger()

class DummyMessage:
    def __init__(self, content):
        self.content = content

@patch("random.randint", return_value=1)
def test_match_true_on_valid_length_and_lucky_chance(mock_randint):
    message = DummyMessage("A short message")
    assert trigger.match(message) is True

@patch("random.randint", return_value=5)
def test_match_false_due_to_random_chance(mock_randint):
    message = DummyMessage("A short message")
    assert trigger.match(message) is False

@patch("random.randint", return_value=1)
def test_match_false_due_to_length(mock_randint):
    message = DummyMessage("x" * (trigger.MAX_LENGTH + 1))
    assert trigger.match(message) is False