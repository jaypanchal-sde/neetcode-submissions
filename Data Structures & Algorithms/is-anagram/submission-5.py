class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        letter_counter = {}
        for i in s:
            if i not in letter_counter:
                letter_counter[i] = 1
            else:
                letter_counter[i] += 1
            
        for i in t:
            if i not in letter_counter:
                return False

            letter_counter[i] -=1
            if letter_counter[i] == 0:
                del letter_counter[i]
        return len(letter_counter) == 0
