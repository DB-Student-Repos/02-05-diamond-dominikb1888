import string


def rows(letter):
    """Produces Diamond of Chars"""
    alphabet = string.ascii_uppercase
    i = alphabet.index(letter)
    whitespace = lambda l, i: " " * (l - i)

    return [
        f"{whitespace(i,line)}"
        + f"{alphabet[line] if line>0 else ''}"
        + f"{alphabet[line]: >{line*2}}"
        + f"{whitespace(i,line)}"
        for line in list(range(i + 1)) + list(reversed(range(i)))
    ]
