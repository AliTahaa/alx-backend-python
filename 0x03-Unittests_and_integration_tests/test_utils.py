#!/usr/bin/env python3
"""a module for testing the utils module."""
import unittest
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """tests the access_nested_map function."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_dict: Dict,
            keys: Tuple[str],
            expected_value: Union[Dict, int],
            ) -> None:
        """tests access_nested_map's output."""
        self.assertEqual(access_nested_map(nested_dict, keys), expected_value)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_dict: Dict,
            keys: Tuple[str],
            expected_exception: Exception,
            ) -> None:
        """tests `access_nested_map`'s exception raising."""
        with self.assertRaises(expected_exception):
            access_nested_map(nested_dict, keys)


class TestGetJson(unittest.TestCase):
    """tests the get_json function."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
            self,
            url: str,
            payload: Dict,
            ) -> None:
        """tests `get_json`'s output."""
        mock_attrs = {'json.return_value': payload}
        with patch("requests.get", return_value=Mock(**mock_attrs)) as mock_get:
            self.assertEqual(get_json(url), payload)
            mock_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """tests the memoize function."""
    def test_memoize(self) -> None:
        """tests memoize's output."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
                ) as mock_method:
            test_instance = TestClass()
            self.assertEqual(test_instance.a_property(), 42)
            self.assertEqual(test_instance.a_property(), 42)
            mock_method.assert_called_once()
