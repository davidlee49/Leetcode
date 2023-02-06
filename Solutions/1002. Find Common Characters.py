class Solution(object):
    def commonChars(self, words):
        # create counter for the first word
        letters = Counter(words[0])
        output = []

        for word in words:
            cur_word = Counter(word)

            for letter in letters:
                if cur_word[letter] < letters[letter]:
                    letters[letter] = cur_word[letter]

        for letter in letters:
            output += [letter] * letters[letter]

        return output