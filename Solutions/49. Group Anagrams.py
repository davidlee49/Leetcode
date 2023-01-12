# https://leetcode.com/problems/group-anagrams/


strs = ["eat","tea","tan","ate","nat","bat"]
def groupAnagrams(strs):
    answer = []
    anagram_count = 0
    anagrams = {
        # {('e',1), ('a',1), ('t',1)} = 0 #["eat", "tea", "ate"]
    }


    for word in strs:
        letter_count = {}
        for char in word:
            if char not in letter_count:
                letter_count[char] = 1
            else:
                letter_count[char] += 1

        anagram = frozenset(letter_count.items())
        if anagram not in anagrams:
            anagrams[anagram] = anagram_count
            answer.append([word])
            anagram_count += 1
        else:
            answer[anagrams[anagram]].append(word)

    return answer

print(groupAnagrams(strs))

