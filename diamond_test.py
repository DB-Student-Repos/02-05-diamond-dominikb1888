import unittest

from diamond import Diamond, DiamondTiles

# Tests adapted from `problem-specifications//canonical-data.json`


class DiamondTest(unittest.TestCase):
    def test_degenerate_case_with_a_single_a_row(self):
        result = ["A"]
        self.assertEqual(Diamond("A").rows, result)

    def test_degenerate_case_with_no_row_containing_3_distinct_groups_of_spaces(self):
        result = [" A ", "B B", " A "]
        self.assertEqual(Diamond("B").rows, result)

    def test_smallest_non_degenerate_case_with_odd_diamond_side_length(self):
        result = ["  A  ", " B B ", "C   C", " B B ", "  A  "]
        self.assertEqual(Diamond("C").rows, result)

    def test_smallest_non_degenerate_case_with_even_diamond_side_length(self):
        result = [
            "   A   ",
            "  B B  ",
            " C   C ",
            "D     D",
            " C   C ",
            "  B B  ",
            "   A   ",
        ]
        self.assertEqual(Diamond("D").rows, result)

    def test_largest_possible_diamond(self):
        result = [
            "                         A                         ",
            "                        B B                        ",
            "                       C   C                       ",
            "                      D     D                      ",
            "                     E       E                     ",
            "                    F         F                    ",
            "                   G           G                   ",
            "                  H             H                  ",
            "                 I               I                 ",
            "                J                 J                ",
            "               K                   K               ",
            "              L                     L              ",
            "             M                       M             ",
            "            N                         N            ",
            "           O                           O           ",
            "          P                             P          ",
            "         Q                               Q         ",
            "        R                                 R        ",
            "       S                                   S       ",
            "      T                                     T      ",
            "     U                                       U     ",
            "    V                                         V    ",
            "   W                                           W   ",
            "  X                                             X  ",
            " Y                                               Y ",
            "Z                                                 Z",
            " Y                                               Y ",
            "  X                                             X  ",
            "   W                                           W   ",
            "    V                                         V    ",
            "     U                                       U     ",
            "      T                                     T      ",
            "       S                                   S       ",
            "        R                                 R        ",
            "         Q                               Q         ",
            "          P                             P          ",
            "           O                           O           ",
            "            N                         N            ",
            "             M                       M             ",
            "              L                     L              ",
            "               K                   K               ",
            "                J                 J                ",
            "                 I               I                 ",
            "                  H             H                  ",
            "                   G           G                   ",
            "                    F         F                    ",
            "                     E       E                     ",
            "                      D     D                      ",
            "                       C   C                       ",
            "                        B B                        ",
            "                         A                         ",
        ]
        self.assertEqual(Diamond("Z").rows, result)

    def test_lc_degenerate_case_with_a_single_a_row(self):
        result = ["a"]
        self.assertEqual(Diamond("a").rows, result)

    def test_lc_degenerate_case_with_no_row_containing_3_distinct_groups_of_spaces(
        self,
    ):
        result = [" a ", "b b", " a "]
        self.assertEqual(Diamond("b").rows, result)

    def test_lc_smallest_non_degenerate_case_with_odd_diamond_side_length(self):
        result = ["  a  ", " b b ", "c   c", " b b ", "  a  "]
        self.assertEqual(Diamond("c").rows, result)

    def test_lc_smallest_non_degenerate_case_with_even_diamond_side_length(self):
        result = [
            "   a   ",
            "  b b  ",
            " c   c ",
            "d     d",
            " c   c ",
            "  b b  ",
            "   a   ",
        ]
        self.assertEqual(Diamond("d").rows, result)

    def test_lc_degenerate_case_with_a_single_a_row(self):
        result = ["0"]
        self.assertEqual(Diamond("0").rows, result)

    def test_lc_degenerate_case_with_no_row_containing_3_distinct_groups_of_spaces(
        self,
    ):
        result = [" 0 ", "1 1", " 0 "]
        self.assertEqual(Diamond("1").rows, result)

    def test_lc_smallest_non_degenerate_case_with_odd_diamond_side_length(self):
        result = ["  0  ", " 1 1 ", "2   2", " 1 1 ", "  0  "]
        self.assertEqual(Diamond("2").rows, result)

    def test_lc_smallest_non_degenerate_case_with_even_diamond_side_length(self):
        result = [
            "   0   ",
            "  1 1  ",
            " 2   2 ",
            "3     3",
            " 2   2 ",
            "  1 1  ",
            "   0   ",
        ]
        self.assertEqual(Diamond("3").rows, result)

    def test_sum(self):
        result = [
            "   A   ",
            "  B B  ",
            " C   C ",
            "  B B  ",
            "   A   ",
            "   A   ",
            "  B B  ",
            " C   C ",
            "D     D",
            " C   C ",
            "  B B  ",
            "   A   ",
        ]
        summing = Diamond("C") + Diamond("D")
        self.assertEqual(summing.split("\n"), result)


if __name__ == "__main__":
    unittest.main()
