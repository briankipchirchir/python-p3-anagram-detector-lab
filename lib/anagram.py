# your code goes here!
# lib/anagram.py

class Anagram:
    def __init__(self, word):
        """
        Initialize the Anagram class with a word.
        :param word: The word to find anagrams for.
        """
        self.word = word

    def match(self, word_list):
        """
        This method finds and returns all anagrams of the stored word from the given word list.
        :param word_list: A list of possible anagram words.
        :return: A list of words from word_list that are anagrams of self.word.
        """
        # Sort the letters of the original word to compare
        sorted_word = sorted(self.word)
        
        # List comprehension to filter out the anagrams
        return [word for word in word_list if sorted(word) == sorted_word]
