#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/24 17:54
@Author  : alexanderwu
@File    : test_token_counter.py
"""
import pytest

from metagpt.utils.token_counter import count_message_tokens, count_output_tokens


def test_count_message_tokens():
    messages = [
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hi there!"},
    ]
    assert count_message_tokens(messages) == 15


def test_count_message_tokens_with_name():
    messages = [
        {"role": "user", "content": "Hello", "name": "John"},
        {"role": "assistant", "content": "Hi there!"},
    ]
    assert count_message_tokens(messages) == 17


def test_count_message_tokens_empty_input():
    """Empty input should return 3 tokens"""
    assert count_message_tokens([]) == 3


def test_count_message_tokens_invalid_model():
    """Invalid model should raise a KeyError"""
    messages = [
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hi there!"},
    ]
    with pytest.raises(NotImplementedError):
        count_message_tokens(messages, model="invalid_model")


def test_count_message_tokens_gpt_4():
    messages = [
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hi there!"},
    ]
    assert count_message_tokens(messages, model="gpt-4-0314") == 15


def test_count_string_tokens():
    """Test that the string tokens are counted correctly."""

    string = "Hello, world!"
    assert count_output_tokens(string, model="gpt-3.5-turbo-0301") == 4


def test_count_string_tokens_empty_input():
    """Test that the string tokens are counted correctly."""

    assert count_output_tokens("", model="gpt-3.5-turbo-0301") == 0


def test_count_string_tokens_gpt_4():
    """Test that the string tokens are counted correctly."""

    string = "Hello, world!"
    assert count_output_tokens(string, model="gpt-4-0314") == 4


if __name__ == "__main__":
    pytest.main([__file__, "-s"])
