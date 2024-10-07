class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        def time(pos,speed):
            time = (target - pos)/speed 
            return time
        arr = []
        stack = []
        for i in zip(position, speed):
            arr.append(i)
        arr.sort()
        arr = arr[::-1]
        for j in range(0,len(arr)):
            t = time(arr[j][0],arr[j][1])
            if not len(stack) or t > stack[-1]:
                stack.append(t)

        return len(stack)
