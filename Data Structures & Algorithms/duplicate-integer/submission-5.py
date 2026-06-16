class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = defaultdict(list)

        for n in nums:
            res[n].append(n)

        return len(res) < len(nums)
     