import unittest
from lab5.Task2.src.TreeHeightCalculator import TreeHeightCalculator

class TestTreeHeightCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = TreeHeightCalculator()

    def test_given_tree_when_calculate_height_then_correct(self):
        # GIVEN
        n = 5
        parents = [4, -1, 4, 1, 1]
        # WHEN
        result = self.calc.tree_height(n, parents)
        # THEN
        self.assertEqual(result, 3)

    def test_given_another_tree_when_calculate_height_then_correct(self):
        # GIVEN
        n = 5
        parents = [-1, 0, 4, 0, 3]
        # WHEN
        result = self.calc.tree_height(n, parents)
        # THEN
        self.assertEqual(result, 4)

    def test_given_binary_tree_when_calculate_height_then_correct(self):
        # GIVEN
        n = 7
        parents = [-1, 0, 0, 1, 1, 2, 2]
        # WHEN
        result = self.calc.tree_height(n, parents)
        # THEN
        self.assertEqual(result, 3)

    def test_given_deep_tree_when_calculate_height_then_correct(self):
        # GIVEN
        n = 10
        parents = [-1,0,1,2,3,4,5,6,7,8]
        # WHEN
        result = self.calc.tree_height(n, parents)
        # THEN
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()