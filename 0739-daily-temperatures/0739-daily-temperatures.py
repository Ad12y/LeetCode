class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0]*len(temperatures)

        for i in range(0, len(temperatures)):
            if not len(stack) or stack[-1][-1] > temperatures[i]:
                stack.append([i, temperatures[i]]) 
            elif stack[-1][-1] <= temperatures[i]:
                while stack and stack[-1][-1] < temperatures[i]:
                    j = stack.pop()[0]
                    answer[j] = i-j
                stack.append([i, temperatures[i]]) 
        print(stack)
        return answer
        
                

        