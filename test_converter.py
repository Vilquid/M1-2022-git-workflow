from unittest import TestCase

from converter import dec_to_bin, bin_to_dec


class TestConverter(TestCase):
    def test_dec_to_bin_even(self):
        n = 10
        expected = [1, 0, 1, 0]
        self.assertListEqual(expected, dec_to_bin(n))

    def test_dec_to_bin_odd(self):
        n = 37
        expected = [1, 0, 0, 1, 0, 1]
        self.assertListEqual(expected, dec_to_bin(n))

    def test_bin_to_dec_odd(self):
        bits = [1, 0, 0, 1, 0, 1]
        expected = 37
        self.assertEqual(expected, bin_to_dec(bits))

    def test_bin_to_dec_even(self):
        bits = [1, 0, 1, 0]
        expected = 10
        self.assertEqual(expected, bin_to_dec(bits))

    def test_reverse(self):
        n = 135
        self.assertEqual(n, bin_to_dec(dec_to_bin(n)))
