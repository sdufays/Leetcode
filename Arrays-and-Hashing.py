from typing import List

class Solution:
    #easy
    def containsDuplicate(self, nums: List[int]) -> bool:
        # visited set, iterate over lst
        visited = set()
        for num in nums:
            if num in dict:
                return True
            visited.add(num)
        return False
    
    #easy
    def isAnagram(self, s: str, t: str) -> bool:
        # compare .count for every letter
        if len(s) != len(t):
            return False
        for letter in set(s):
            if s.count(letter) != t.count(letter):
                return False
        return True

    #easy
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash map, complement
        hash_map = {}
        for i, number in enumerate(nums):
            if number not in hash_map:
                hash_map[number] = i
            complement = target - number
            if complement in hash_map and hash_map[complement] != i:
                return [hash_map[complement], i]
    
    #medium

        
