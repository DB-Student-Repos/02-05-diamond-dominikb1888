import string


def rows(letter):
    """Produces Diamond of Chars"""
    a = string.ascii_uppercase
    l = a.index(letter)
    w = lambda l, i: " " * (l - i)
    result = [
        f"{w(l,i)}{a[i] if i>0 else ''}{a[i]: >{i*2}}{w(l,i)}" for i in range(0, l + 1)
    ]
    return "\n".join(result + result[-2::-1]).split("\n")
