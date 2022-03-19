import string


def rows(letter):
    """produces diamond"""
    letters = string.ascii_uppercase
    num = letters.index(letter)
    result = []
    result.append(" " * num + "A" + " " * num)

    for i, char in enumerate(letters[1: num + 1]):
        result.append(
            " " * (num - i - 1) + char + " " *
            (i * 2 + 1) + char + " " * (num - i - 1)
        )

    return result + [res for res in result[-2::-1]]
