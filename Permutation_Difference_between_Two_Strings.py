
##Tags:Leetcode_Easy_HashTable_String_Accenture_Microsoft
#You are given two strings s and t such that every character occurs at most once in s and t is a permutation of s.
#The permutation difference between s and t is defined as the sum of the absolute difference between the index of the occurrence ofeach character in s and the index of the occurrence of the same character in t.
#Return the permutation difference between s and t.

#Code:

class Solution(object):
    def findPermutationDifference(s, t):
        indices_in_s={ }#calculating the indices of each characters in string s
        for i,char in enumerate(s):
            indices_in_s[char]=i
        indices_in_t={ }#calculating the indices of each characters in string t
        for i,char in enumerate(t):
            indices_in_t[char]=i
        abs_diff =[ ] #finding the absolute differences
        for char in indices_in_s:
            diff=abs(indices_in_s[char]-indices_in_t[char])
            abs_diff.append(diff)
        permutation_diff=sum(abs_diff) #adding the absolute differences of each character.
        return permutation_diff
if __name__ == "__main__":
    s = "abcde"
    t = "edcba"
    result = Solution.findPermutationDifference(s,t)
    print(f"The permutation difference between '{s}' and '{t}' is: {result}")
