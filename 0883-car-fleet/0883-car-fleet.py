class Solution(object):
    def carFleet(self, target, position, speed):
        stack = []
        ps = [(p,s) for p, s in zip(position, speed)]
        ps.sort()
        print(ps)
        for i in reversed(ps):
            t = float(target - i[0])/i[1]
            print(t)
            if len(stack) == 0 or t > stack[-1]:
                stack.append(t)
        print(stack)
        return len(stack)

        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        