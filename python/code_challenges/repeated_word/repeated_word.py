from code_challenges.hashtable.hash_table import HashTable
import string
"""[Module with a method for finding the first repeated word
in a string of any length. Requires a HashTable]
"""

def first_repeat(long_str):
    """[returns the first repeated word in a string]

    Args:
        long_str ([str]): [may be a string of any length]
    """
    long_str = long_str.lower().split()
    table = HashTable(size=1024)

    for word in long_str:
        word = word.strip(str(string.punctuation))
        if table.contains(word):
            return word
        else:
            table.add(word, word)
            continue

    return f'no repeated words found'
