import unittest
from lab6.Task5.src.ElectionsProcessor import ElectionsProcessor

class TestElectionsProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = ElectionsProcessor()

    def test_given_candidates_when_process_then_sorted_result(self):
        # GIVEN
        data = [
            ("candidateA", "100"),
            ("candidateC", "50"),
            ("candidateB", "70")
        ]
        # WHEN
        result = self.processor.process_elections(data)
        # THEN
        self.assertEqual(result, ["candidateA 100\n", "candidateB 70\n", "candidateC 50\n"])


if __name__ == '__main__':
    unittest.main()