from converter import dec_to_bin, bin_to_dec


def say_hello():
    print("Hello")


if __name__ == '__main__':
    print(*dec_to_bin(256))
    print(bin_to_dec([1, 0, 1, 0, 0, 1]))
