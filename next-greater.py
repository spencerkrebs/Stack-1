# O(n) time, O(1) space
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1]*n
        stack=[]
        for i in range(2*n):
            num = nums[i%n]
            while stack and nums[stack[-1]] < num:
                poppedIndex = stack.pop()
                res[poppedIndex]=num 

            if i < n:
                stack.append(i)

        return res