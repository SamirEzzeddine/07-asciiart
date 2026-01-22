"""
ASCII Art encoding (run-length encoding).

This module provides two functions to encode a string into a list of
(character, count) tuples using iterative and recursive approaches.
"""

#### Imports et définition des variables globales

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    """Encode a string using an iterative algorithm.

    Args:
        s (str): the string to encode

    Returns:
        list: list of tuples (character, consecutive occurrences)
    """
    if s == "":
        return []

    characters = [s[0]]
    occurrences = [1]
    k = 1
    n = len(s)

    while k < n:
        if s[k] == s[k - 1]:
            occurrences[-1] += 1
        else:
            characters.append(s[k])
            occurrences.append(1)
        k += 1

    return list(zip(characters, occurrences))


def artcode_r(s):
    """Encode a string using a recursive algorithm.

    Args:
        s (str): the string to encode

    Returns:
        list: list of tuples (character, consecutive occurrences)
    """
    # cas de base
    if s == "":
        return []

    first_char = s[0]
    count = 1

    while count < len(s) and s[count] == first_char:
        count += 1

    return [(first_char, count)] + artcode_r(s[count:])


#### Fonction principale


def main():
    """Test the iterative and recursive ASCII art encoders."""
    test_string = "MMMMaaacXolloMM"
    print(artcode_i(test_string))
    print(artcode_r(test_string))


if __name__ == "__main__":
    main()
