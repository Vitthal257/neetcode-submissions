class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        gp = sorted(zip(position, speed), reverse=True)
        stk=[]
        for pos, speed in gp:
            time = (target-pos)/speed
            if len(stk) != 0 and stk[-1] >= time:
                continue
            stk.append(time)

        return len(stk)