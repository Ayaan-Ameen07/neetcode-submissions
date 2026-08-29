class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        timestack = []

        for p, s in sorted(pair, reverse=True):
            x = (target - p) / s
            if not timestack or x > timestack[-1]:
                timestack.append(x)
            # else: this car catches up to the fleet ahead, so it merges — don't push

        return len(timestack)