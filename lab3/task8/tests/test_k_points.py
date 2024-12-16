import unittest
from lab3.task8.scr.k_points import get_k_closest_points


class TestGetKClosestPoints(unittest.TestCase):
    def test_should_return_k_closest_points(self):
        # GIVEN
        points = [(1, 2), (4, 5), (0, 1), (3, 3)]
        k = 2
        expected_output = [(0, 1), (1, 2)]

        # WHEN
        result = get_k_closest_points(points, k)

        # THEN
        self.assertEqual(result, expected_output)

    def test_should_return_all_points_when_k_equals_length(self):
        # GIVEN
        points = [(1, 2), (4, 5), (0, 1)]
        k = 3
        expected_output = [(0, 1), (1, 2), (4, 5)]

        # WHEN
        result = get_k_closest_points(points, k)

        # THEN
        self.assertEqual(result, expected_output)

    def test_should_handle_empty_points_list(self):
        # GIVEN
        points = []
        k = 2
        expected_output = []

        # WHEN
        result = get_k_closest_points(points, k)

        # THEN
        self.assertEqual(result, expected_output)

    def test_should_handle_k_equals_zero(self):
        # GIVEN
        points = [(1, 2), (4, 5), (0, 1)]
        k = 0
        expected_output = []

        # WHEN
        result = get_k_closest_points(points, k)

        # THEN
        self.assertEqual(result, expected_output)

    def test_should_return_closest_points_when_points_have_negative_coordinates(self):
        # GIVEN
        points = [(1, 2), (-1, -1), (3, 4), (-2, -2)]
        k = 2
        expected_output = [(-1, -1), (1, 2)]

        # WHEN
        result = get_k_closest_points(points, k)

        # THEN
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
