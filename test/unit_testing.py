import unittest

import core

class CodeUnitTesting(unittest.TestCase):

    # Anagram Test Cases
    def test_anagram_empty(self):
        self.assertEqual([], core.anagram("abab", ["babaa", "aaab", "aabba"]))

    def test_anagram_one_word(self):
        self.assertEqual(["aabb"], core.anagram("abab", ["babaa", "aabb", "aabba"]))

    def test_anagram_two_words(self):
        self.assertEqual(['bbaa', 'aabb'], core.anagram("abab", ["bbaa", "aabb", "aabba"]))

    def test_anagram_main_str_none(self):
        self.assertEqual([], core.anagram("", ["bbaa", "aabb", "aabba"]))

    def test_anagram_numbers(self):
        self.assertEqual([], core.anagram("", ["123", "321", "423"]))

    # Date Calculation Test Cases
    def test_date_calculation_sat(self):
            self.assertEqual("01/09/2018", core.date_calculation("01/09/2018"))

    def test_date_calculation_wed(self):
        self.assertEqual("05/09/2018", core.date_calculation("02/09/2018"))

    def test_date_calculation_sat_case2(self):
        self.assertEqual("08/09/2018", core.date_calculation("07/09/2018"))

    def test_date_calculation_wed_case2(self):
        self.assertEqual("05/09/2018", core.date_calculation("04/09/2018"))

    def test_date_calculation_raise_exception(self):
        with self.assertRaises(ValueError):
            core.date_calculation("12/24/2018")

    # LRU implementation Test Cases, Assuming Cache size 5
    def lru_key1(self):
        self.assertEqual(3500, core.to_be_cached(3, 5))

    def lru_key2(self):
        self.assertEqual(4500, core.to_be_cached(4, 5))

    def lru_key3(self):
        self.assertEqual(5500, core.to_be_cached(5, 5))

    def lru_key4(self):
        self.assertEqual(6500, core.to_be_cached(6, 5))

    # Since the key (3,5) is already computed and stored in cache, there will be no
    # computation for this call, rather the data will be returned from the cache based on LRU
    # Algorithm.
    def lru_key5(self):
        self.assertEqual(3500, core.to_be_cached(3, 5))


if __name__ == '__main__':
    unittest.main()
