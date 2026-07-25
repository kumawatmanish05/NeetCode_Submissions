'''The optimal solution uses a Python set(), which stores only unique elements.
We create an empty set called seen and traverse the array one element at a time. 
For each element, we first check if it already exists in the seen set. 
If it does, we immediately return True because a duplicate has been found. 
If it is not present, we add the element to the set and continue. 
If we finish traversing the entire array without finding any duplicate, we return False.
Since checking and inserting elements into a set takes O(1) average time, the overall time complexity is O(n),
where n is the number of elements. The space complexity is O(n) because, in the worst case, all elements are unique and are stored in the set. 
This approach is preferred in interviews because it is simple, efficient, and uses hashing to achieve linear time complexity. ''' 


#Solution 1 : Using Set  

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False 

#Solution 2 : Using Sorting

def containsDuplicate(nums):
    nums.sort()

    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True

    return False




        
