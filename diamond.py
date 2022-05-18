import string
import functools


class Diamond:
    def __init__(self, char, case="upper"):
        self.chars = (
            string.ascii_uppercase if case == "upper" else string.ascii_lowercase
        )
        self.index = self.chars.index(char)

    @staticmethod
    def _join(func):
        @functools.wraps(func)
        def wrapper_join(*args, **kwargs):
            result = func(*args, **kwargs)
            return "\n".join(result)

        return wrapper_join

    @_join
    def __add__(self, other):
        swidth = len(self.rows[0])
        owidth = len(other.rows[0])
        margin = abs(swidth - owidth) // 2

        if swidth < owidth:
            return self._add_margin(self, margin) + other.rows
        elif swidth > owidth:
            return self.rows + self._add_margin(other, margin)
        else:
            return self.rows + other.rows

    def __radd__(self, other):
        return self.__add__(self, other) if isinstance(other, Diamond) else self

    def __repr__(self):
        return "\n".join(self.rows)

    def __str__(self):
        return self.__repr__()

    @property
    def rows(self):
        return [
            f"{self.chars[j]:>{i}}{self.chars[j] if j>0 else '':>{j*2}}{' '*(i-1)}"
            for j, i in self._gen_lists(self.index)
        ]

    @staticmethod
    def _gen_lists(n):
        return zip(
            list(range(n + 1)) + list(reversed(range(0, n))),
            list(range(n + 1, 1, -1)) + list(reversed(range(n + 1, 0, -1))),
        )

    @staticmethod
    def _add_margin(smaller, margin):
        return [(" " * margin + row + " " * margin) for row in smaller.rows]


class DiamondTiles(Diamond):
    def __init__(self, diamonds, columns=2):
        self.diamonds = [
            diamond for diamond in diamonds if isinstance(diamond, Diamond)
        ]
        self.columns = columns

    def __repr__(self):
        columns = []
        window = len(self.diamonds) // self.columns
        for i in range(0, len(self.diamonds) + 1, window):
            columns.append(sum(self.diamonds[i : i + window]))

        return "\n".join(
            [str(diamonds) for diamonds in columns if isinstance(diamonds, Diamond)]
        )
