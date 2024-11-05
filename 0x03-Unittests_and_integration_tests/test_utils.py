#!/usr/bin/env python3
"""Module for testing utility functions."""

import unittest
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for `access_nested_map` function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Dict, path: Tuple[str], expected: Union[Dict, int]) -> None:
        """Test `access_nested_map` returns correct output."""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map: Dict, path: Tuple[str], exception: Exception) -> None:
        """Test `access_nested_map` raises correct exceptions."""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test cases for `get_json` function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """Test `get_json` returns correct output."""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch("requests.get", return_value=mock_response) as mock_get:
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test cases for `memoize` function."""

    def test_memoize(self) -> None:
        """Test `memoize` decorator."""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as mock_method:
            instance = TestClass()
            self.assertEqual(instance.a_property(), 42)
            self.assertEqual(instance.a_property(), 42)
            mock_method.assert_called_once()
