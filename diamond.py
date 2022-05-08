import string


def rows(char):
    a = string.ascii_uppercase
    n = a.index(char)
    return [
        f"{a[j]:>{i}}{a[j] if j>0 else '':>{j*2}}{' '*(i-1)}"
        for j, i in zip(
            list(range(n + 1)) + list(reversed(range(0, n))),
            list(range(n + 1, 1, -1)) + list(reversed(range(n + 1, 0, -1))),
        )
    ]
