#!/usr/bin/env python3
"""Parameterize a unit test """
from parameterized import parameterized
from unittest import TestCase
from unittest.mock import patch
from utils import *


class TestAccessNestedMap(TestCase):
    """ Test access_nested_map from utils.py """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(err.exception))

class TestGetJson(TestCase):
    """ Test utils.get_json function"""

    @parameterized.expand([("http://example.com", {
        "payload": True}), ("http://holberton.io", {"payload": False})])
    @patch('test_utils.get_json')
    def test_get_json(self, test_url, test_payload, mock):
        """ Test that utils.get_json """

        mock.return_value = test_payload
        res = get_json(test_url)
        self.assertEqual(res, test_payload)


class TestMemoize(TestCase):
    """ Test utils.memoize function """

    def test_memoize(self):
        """ Test memorize method"""

        class TestClass:
            """ Attributes to test memoize"""

            def a_method(self):
                """ Returns an instance of memoize class"""

                return 42

            @memoize
            def a_property(self):
                """ Method that defines instance of memoize"""

                return self.a_method()

        with patch.object(TestClass, "a_method") as mock:
            test = TestClass()
            test.a_property
            test.a_property
            mock.assert_called_once
