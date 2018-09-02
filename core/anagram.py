"""
Find an Anagram

Developer: Dev Team,
Last Modified Date:
"""
from collections import Counter


def anagram(main_str, str_list):
    """
    This function will finds the valid anagrams of the main_str from the
    given input string list.

    Input: Main String and String list
    :return: List of a valid anagrams of a given string from the input list.
    """
    return [_str for _str in str_list if str_list and Counter(_str) == Counter(main_str)]


if __name__ == "__main__":
    print (anagram("abab", ["babaa", "aaab", "aabba"]))
