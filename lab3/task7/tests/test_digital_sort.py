import unittest
from lab3.task7.scr.digital_sort import counting_sort, digital_sort
import os

class TestDigitalSort(unittest.TestCase):
    def setUp(self):
        """Настройка тестового окружения."""
        self.input_path = 'input.txt'
        self.output_path = 'output.txt'

    def test_counting_sort(self):
        # Given
        strings = ["bab", "bba", "baa"]
        index = 2

        # When
        sorted_strings = counting_sort(strings, index)

        # Then
        self.assertEqual(
            sorted_strings,
            ["bba", "baa", "bab"],  # Правильный результат
            "Сортировка по последнему символу должна возвращать ['bba', 'baa', 'bab']."
        )

    def test_digital_sort(self):
        # Given
        strings = ["bab", "bba", "baa"]
        k = 2
        m = 3

        # When
        sorted_strings = digital_sort(strings, k, m)

        # Then
        self.assertEqual(
            sorted_strings,
            ["baa", "bab", "bba"],  # Правильный результат
            "Цифровая сортировка должна возвращать ['baa', 'bab', 'bba']."
        )


    def tearDown(self):
        """Очистка тестового окружения."""
        if os.path.exists(self.input_path):
            os.remove(self.input_path)
        if os.path.exists(self.output_path):
            os.remove(self.output_path)


if __name__ == '__main__':
    unittest.main()
