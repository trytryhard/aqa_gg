"""list preparation module"""


def list_inting(input_list: list) -> list[int]:
    """
    apply logic to list : [int(x) for x in value]
    with raise VallErr on exceptions

    if all is fine return result of [int(x) for x in value]
    """
    ans = []

    for i in input_list:
        temp = i
        try:
            temp = int(float(temp))
        except ValueError as e:
            raise ValueError(f"{i} - Invalid input") from e
        ans.append(temp)

    return ans
