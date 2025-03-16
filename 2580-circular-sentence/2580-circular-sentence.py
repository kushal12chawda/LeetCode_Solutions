class Solution(object):
    def isCircularSentence(self, sentence):
        words = sentence.split()
        if words[0][0] != words[-1][-1]:
            return False
        return all(words[i][-1] == words[i + 1][0] for i in range(len(words) - 1))
            