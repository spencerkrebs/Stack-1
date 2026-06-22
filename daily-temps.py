# O(n) time because it's a monotonic stack
# each element is pushed into and popped from the stack exactly once
# Imagine a week of steadily dropping temperatures, followed by a sudden heatwave on the last day:
# [90, 80, 70, 60, 50, 95]
# As the temperatures drop, the while loop never triggers. Every single day is colder than the day before. They all just get pushed straight onto the stack.
# Stack: [90, 80, 70, 60, 50]
# while loop not triggered until last day
# O(n) space 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)

        stack=[]
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                res[stackIndex]=(i-stackIndex)
            stack.append([t,i])

        return res


#      0 1 2 3 4 5 6 7        
# res=[1,1,4,2,1,1,0,0]
# stackTemp = 72 , stackIndex= 5
# stack = [[76,6]]
# 73,74,75,71,69,72,76,73
#  0. 1. 2. 3  4. 5. 6  7
#                       i