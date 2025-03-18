class Solution(object):
    def longestWord(self, words):
        words.sort()
        word_set, longest = set([""]), ""

        for word in words:
            if word[:-1] in word_set:
                word_set.add(word)
                if len(word) > len(longest):
                    longest = word
        
        return longest