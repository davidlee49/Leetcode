class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Intuition, this will likely take n2:
        # the gas reserve determines if we can keep going and is based on
        # and depends on the previous location. basically starting position mattters

        # we could use dp to precalculate gas input/output but would still be n2

        gas_netgain = []
        gas_reserves = 0
        gas_needed = 0
        start = None

        # get differences #get sum
        for i in range(len(gas)):
            gas_netgain.append(gas[i] - cost[i])

        # -2, -2, -2, 3, 3
        for i, gas in enumerate(gas_netgain):
            if start == None:
                start = i
            gas_reserves += gas
            if gas_reserves < 0:
                start = None
                gas_needed += gas_reserves
                gas_reserves = 0

        if gas_reserves + gas_needed >= 0:
            return start
        else:
            return -1