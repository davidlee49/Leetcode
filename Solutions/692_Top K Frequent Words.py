#https://leetcode.com/problems/top-k-frequent-words/


words = ["the","day","is","sunny","the","the","the","sunny","is","is", "hi", "hi", "hi", "hi"]
k = 4

def topKFrequent(words, k):
    word_freq = {

    }
    k_word_freq = []
    k_word_freq_sorted = []
    highest_freq = 0

    for word in words:  # eval each word
        if word not in word_freq:  # keep track of word/freq
            word_freq[word] = 1
        else:
            word_freq[word] += 1
            if word_freq[word] > highest_freq:
                highest_freq = word_freq[word]
    x = list(word_freq.values())
    print(x)


    # x.sort(reverse=True)
    # print(x)
    # while len(k_word_freq_sorted) < k:
    #     highest_freq =
    #     k_word_freq_sorted = [word for word in x if word[]]


    # while len(k_word_freq_sorted) < k:



    # while k > 0:
    #     sort_words = [word for word in word_freq if word_freq[word] == k]
    #     sort_words.sort()
    #     print(sort_words)
    #     while len(k_word_freq_sorted) < k:
    #         k_word_freq_sorted.append(sort_words[0])
    #         k -= 1

    # print(k_word_freq_sorted)

    # pick matching word freq with k
    # if len(k_word_freq) > 1:
    #     while k_word_freq:

    # eval by char

    # return k_word_freq

topKFrequent(words, k)

