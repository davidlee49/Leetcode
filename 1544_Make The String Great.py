

s = "s"


def makeGood(s: str) -> str:

    letters = []
    for char in s:
        if letters and char.swapcase() == letters[-1]:
            letters.pop()
        else:
            letters.append(char)

    return "".join(letters)

print(makeGood((s)))