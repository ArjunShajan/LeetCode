class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited={}
        for i in range(len(nums)):
            element=target-nums[i]
            if element in visited:
                j=visited[element]
                return[i,j]
            visited[nums[i]]=i