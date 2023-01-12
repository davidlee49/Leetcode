class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        #return word.isupper() or word.islower() or word.istitle() #o(3n) solution
        if word[0].islower():
            return word.islower()
        else:
            return word.istitle() or word.isupper()