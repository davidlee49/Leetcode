arr = ["un","iq","ue"]

def maxLength(arr):
    max_len = ""
    for i in arr:
        max_len += i
    max_len = len(set(max_len))
    def find_combinations(combo_list, sum_of_combination, max_len):
        if sum_of_combination == 1:
            return combo_list

        combinations = []
        for index, combo_base in enumerate(combo_list):
            add_to_base = combo_list[index + 1:]
            add_to_base = find_combinations(add_to_base, sum_of_combination - 1, max_len)

            for partial_combo in add_to_base:
                potential_answer = combo_base + partial_combo
                if len(potential_answer) > max_len:
                    pass

                else:
                    combinations.append(combo_base + partial_combo)

        return combinations

    potential_answer = (0, "")
    for i in range(len(arr),0,-1):
        answer = find_combinations(arr, i, max_len)
        for i in answer:
            if len(i) == len(set(i)):
                if len(i) > potential_answer[0]:
                    potential_answer = (len(i), i)
    if potential_answer[0] != 0:
        return potential_answer[0]
    return 0


print(maxLength(arr))

# r = "abc"
# print(len(set(r))