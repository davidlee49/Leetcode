import collections
def checkInclusion(s1: str, s2: str) -> bool:
    s1_counter = collections.Counter(s1)
    s2_counter = collections.Counter()
    s2_substring_count = 0
    start_i = 0

    for cur_i, char in enumerate(s2):
        if char in s1_counter:
            s2_counter[char] += 1
            s2_substring_count += 1

            while s2_counter[char] > s1_counter[char]:
                s2_counter[s2[start_i]] -= 1
                start_i += 1
                s2_substring_count -= 1

            if s2_substring_count == len(s1):
                return True

        else:
            s2_counter.clear()
            s2_substring_count = 0
            start_i = cur_i + 1

    return False

