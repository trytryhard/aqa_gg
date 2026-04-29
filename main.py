"""entry module"""

from src.compressing import compress_numbers


def main() -> None:
    """entry point"""
    input_console = input("Input list: ").split()
    # inside of function fix list[str] to list[int] in list_inting()
    ans = compress_numbers(input_console)
    print("\nanswer:", ans)


if __name__ == "__main__":
    print(
        "Input ur list of numbers that separated with space-symbol. After that press Enter."
        "\n From floats will be used only integer part. "
        "\n Float writes with DOT(.) instead of comma(,)."
        "\n Examples: 15.4 -> 15; 16,0 -> wrong value \n"
    )
    main()
