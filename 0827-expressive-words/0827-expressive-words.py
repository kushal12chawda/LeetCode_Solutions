class Solution(object):
    def expressiveWords(self, s, words):
        def is_stretchy(base, word):
            i, j = 0, 0
            while i < len(base) and j < len(word):
                if base[i] != word[j]:
                    return False
                
                base_count = 1
                while i + 1 < len(base) and base[i] == base[i + 1]:
                    i += 1
                    base_count += 1
                
                word_count = 1
                while j + 1 < len(word) and word[j] == word[j + 1]:
                    j += 1
                    word_count += 1
                
                if base_count < word_count or (base_count < 3 and base_count != word_count):
                    return False
                
                i += 1
                j += 1
            
            return i == len(base) and j == len(word)

        return sum(1 for word in words if is_stretchy(s, word))