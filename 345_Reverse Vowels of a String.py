#https://leetcode.com/problems/reverse-vowels-of-a-string/

#will take n time to find all the vowels
    # this can be done with 2 pointers
    # i think it can be also done in log n time




# find both lower and uppercase vowels
# because we are doing an immediate replacement, we only need constant space
    #find first vowel, increment l pointer
    #find second vowel, decrement r pointer




def reverseVowels(s):

    vowels = "AEIOUaeiou"
    vowels = set(vowels)
    switch_vowels = ""
    new_string = ""
    last_word = -1
    for char in s:
        if char in vowels:
            switch_vowels = switch_vowels + char

    for char in s:
        if char in vowels:
            new_string = new_string + switch_vowels[last_word]
            last_word -= 1
        else:
            new_string = new_string + char
    return new_string

print(reverseVowels("hello"))



