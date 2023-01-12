class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        # make compairing dictionary
        compare_to_pattern = {}
        used_words = set()

        # split string into individual words array
        words = s.split()

        if len(pattern) != len(words):
            return False
        # iterate with index through words array
        for i, char in enumerate(pattern):
            # add/compare with dictionary
            if char not in compare_to_pattern:
                if words[i] in used_words:
                    return False
                compare_to_pattern[char] = words[i]
                used_words.add(words[i])
            elif compare_to_pattern[char] != words[i]:
                return False

        return True



