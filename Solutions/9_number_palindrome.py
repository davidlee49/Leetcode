
x = -1133553311

def isPalindrome(x):
    if x < 0:
        return False
    x = str(x)
    l,r = 0, len(x)-1
    while l < (len(x) +1)/2:
        if x[l] == x[r]:
            l += 1
            r -= 1
        else:
            return False
    return True

print(isPalindrome(x))


