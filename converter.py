from typing import List


def dec_to_bin(n: int) -> List[int]:
    """
    Converts a positive integer to binary
    :param n: int, decimal integer to convert to binary
    :return: Binary translation of input number, as a list of 0s and 1
    """
    if n < 0:
        raise ValueError("n should be positive")

    bit = [0 if n % 2 == 0 else 1]
    return bit if n <= 1 else dec_to_bin(n >> 1) + bit


def bin_to_dec(bits_array: List[int]) -> int:
    """
    Converts a list of 0s and 1s to its corresponding decimal representation
    :param bits_array: list of 0s and 1s to convert
    :return: int
    """
    if not inputs_is_bits(bits_array):
        raise ValueError("input should contain only bits (0 or 1)")

    ba = bits_array.copy()
    ba.reverse()
    return sum([(1 << i) * m for i, m in enumerate(ba)])


def inputs_is_bits(bits_array):
    for b in bits_array:
        if b not in [0, 1]:
            return False
    return True
