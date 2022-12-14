#https://leetcode.com/problems/reverse-string/

# O n time because we need to visit every element



s = ["H","a","n","n","a","h"]

def reverseString(s):
    beginning = 0
    end = len(s) - 1

    while beginning <= end:
        #swap letters
        temp = s[beginning]
        s[beginning] = s[end]
        s[end] = temp

        #increment/decrement
        beginning += 1
        end -= 1


    return(s)

print(reverseString(s))


