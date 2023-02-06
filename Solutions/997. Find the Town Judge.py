class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # create set for if someone trusts someone else
        # create dict for people that trust someone else
        no_trust = set()
        trust_dict = {}
        for i in range(1, n + 1):
            trust_dict[i] = set()
            no_trust.add(i)

        # iterate through that array
        for truster, trustee in trust:
            no_trust.discard(truster)
            trust_dict[trustee].add(truster)

        # return the person if they are the only person left if set and in the dict, everyone trusts them
        if len(no_trust) == 1:
            potential_judge = no_trust.pop()
            if len(trust_dict[potential_judge]) == n - 1:
                return potential_judge

        return -1



