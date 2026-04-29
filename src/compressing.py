"""compressing module"""

from src.list_preparation import list_inting


def compress_numbers(input_val: list[int]) -> list[int]:
    """
    expect list of separated integer values,
    recheck inputted list,
    apply logic

    return compressed numbers:
    example:
    1. [1, 1, 2, 2, 3] → [1, 2, 3]
    2. [0, 0, 1, 1, 0] → [0, 1, 0]
    """
    input_val = list_inting(input_val)

    ans = []
    if not input_val:
        return ans

    current = None

    for i in input_val:
        if current is not None:
            if i != current:
                ans.append(current)
                current = i
        else:
            current = i
    ans.append(current)

    return ans
