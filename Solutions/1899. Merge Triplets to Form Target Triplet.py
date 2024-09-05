
def mergeTriplets(triplets, target):
    # we could brute force this problem, however it would be an insane time complexity to find every combination
    # we can optimize based on the contraints of the problem, we have to use a max function
        # we can assert that any triplet used can not include a value < the targets respective index
        # knowing this we can reduce all valid triplets in O(n) time
    # lastly we must check to ensure from the valid inputs at least 1 instance of the target[i] exists
    t1, t2, t3 = target
    f1, f2, f3 = False, False, False
    for n1, n2, n3 in triplets:
        if n1 <= t1 and n2 <= t2 and n3 <= t3:
            f1 = f1 or n1 == t1
            f2 = f2 or n2 == t2
            f3 = f3 or n3 == t3

    return f1 and f2 and f3


triplets = [[2,5,3],[1,8,4],[1,7,5]]
target = [2,7,5]
print(mergeTriplets(triplets, target))
