import unittest
from lab5.Task7.src.HeapSorter import HeapSorter

class TestHeapSorter(unittest.TestCase):
    def setUp(self):
        self.sorter = HeapSorter()

    def test_given_array_when_heapify_then_correct_structure(self):
        # GIVEN
        arr = [3, 9, 2, 1, 4]
        # WHEN
        self.sorter.heapify(arr, len(arr), 0)
        # THEN
        self.assertEqual(arr, [9, 4, 2, 1, 3])

    def test_given_desc_array_when_heapsort_then_asc(self):
        # GIVEN
        arr = [5,4,3,2,1]
        # WHEN
        self.sorter.heapsort(arr)
        # THEN
        self.assertEqual(arr, [1,2,3,4,5])

    def test_given_random_array_when_heapsort_then_sorted(self):
        # GIVEN
        arr = [4,10,3,5,1]
        # WHEN
        self.sorter.heapsort(arr)
        # THEN
        self.assertEqual(arr, [1,3,4,5,10])

    def test_given_reverse_array_when_heapsort_then_sorted(self):
        # GIVEN
        arr = [5,4,3,2,1]
        # WHEN
        self.sorter.heapsort(arr)
        # THEN
        self.assertEqual(arr, [1,2,3,4,5])


if __name__ == '__main__':
    unittest.main()