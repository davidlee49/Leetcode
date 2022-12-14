#https://leetcode.com/problems/longest-repeating-character-replacement/


s = "ABBB"
k = 2


def characterReplacement(s, k):
    switch_count = k
    longest_repeating_char = 0
    # iterate through each letter in string counting repeating char + 2 change
    for index, char in enumerate(s):
        potential_subtring = 1
        index += 1
        while index < len(s):
            if s[index] != char:
                if k == 0:
                    break
                k -= 1
            potential_subtring += 1
            index += 1
        longest_repeating_char = max(longest_repeating_char, min(potential_subtring+k, len(s)))
        k = switch_count



    return longest_repeating_char


print(characterReplacement(s, k))