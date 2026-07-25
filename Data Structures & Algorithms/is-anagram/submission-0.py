class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

# Approach 1 : Direct sorting and then equal the string aaagmnr = aaagmnr 
        return sorted(s) == sorted(t)

# Approach 2 : Direct using the inbuilt Count function 
        return Counted(s) == Counted(t)

# Approach 3 : Same as approach 2 but without direct function

        if len(s) != len(t):
            return False

        countS , countT = {},{}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True
#This approach has a time complexity of O(s + t) as it iterates through both strings, and a space complexity of O(s + t) for the hashmap storage.
