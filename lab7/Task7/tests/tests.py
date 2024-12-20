import unittest
from lab7.Task7.src.PatternMatcher import PatternMatcher

class TestMatchesPattern(unittest.TestCase):
    def test_given_identical_when_match_then_yes(self):
        # GIVEN
        # WHEN
        result = PatternMatcher.matches_pattern("abc", "abc")
        # THEN
        self.assertEqual(result, "YES")

    def test_given_question_when_match_then_yes(self):
        # GIVEN
        # WHEN
        result = PatternMatcher.matches_pattern("a?c", "abc")
        # THEN
        self.assertEqual(result, "YES")

    def test_given_asterisk_when_match_then_yes(self):
        # GIVEN
        # WHEN
        result = PatternMatcher.matches_pattern("a*", "abc")
        # THEN
        self.assertEqual(result, "YES")

    def test_given_no_match_when_match_then_no(self):
        # GIVEN
        # WHEN
        result = PatternMatcher.matches_pattern("dog", "cat")
        # THEN
        self.assertEqual(result, "NO")

    def test_given_combo_when_match_then_yes(self):
        # GIVEN
        # WHEN
        result = PatternMatcher.matches_pattern("*a?b", "zaab")
        # THEN
        self.assertEqual(result, "YES")

    def test_given_empty_pattern_when_match_then_no(self):
        # GIVEN
        # WHEN
        result = PatternMatcher.matches_pattern("", "x")
        # THEN
        self.assertEqual(result, "NO")

    def test_given_empty_string_when_asterisk_then_yes(self):
        # GIVEN
        # WHEN
        result = PatternMatcher.matches_pattern("*", "")
        # THEN
        self.assertEqual(result, "YES")

    def test_given_both_empty_when_match_then_yes(self):
        # GIVEN
        # WHEN
        result = PatternMatcher.matches_pattern("", "")
        # THEN
        self.assertEqual(result, "YES")


if __name__ == "__main__":
    unittest.main()