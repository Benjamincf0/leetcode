class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(list(zip(position, speed)), key=lambda x: -1*x[0]) # lol
        
        numFleets = 0
        nextTimeToTarget = 0 # pos is strictly less than target
        for pos, speed in pairs:
            timeToTarget = (target-pos)/speed

            # current is slower than next (or empty stack)
            # => implies they must NOT intersect => new fleet
            if timeToTarget > nextTimeToTarget:
                nextTimeToTarget = timeToTarget
                numFleets += 1

        return numFleets