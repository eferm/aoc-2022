from utils import *


inp = get_input(2022, 6)


def stream_marker(stream, size):
    for i in range(size - 1, len(stream)):
        if len(set(stream[i - size : i])) == size:
            return i

    # return lmap(
    #     lambda i: len(set(stream[i - size : i])) == size,
    #     range(size - 1, len(stream)),
    # ).index(True) + (size - 1)


# part 1
print(stream_marker(inp, 4))

# part 2
print(stream_marker(inp, 14))
