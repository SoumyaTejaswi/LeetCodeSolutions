#Tags:Medium_Array_Amazon_TikTok_Google_PocketGems_Microsoft_Apple_Yahoo_Adobe_Uber_Meta_Bloomberg
#Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice.
#Return an array of all the integers that appears twice.

#code:

class Solution(object):
    def findDuplicates(nums):
        duplicate_array=[ ]
        for i in nums:
            index=abs(i)-1
            if nums[index]<0:
                duplicate_array.append(abs(i))
            else:
                nums[index]=-nums[index]
        return duplicate_array

if __name__=="__main__":
    arr=[4,3,2,7,8,2,3,1]
    result_arr=Solution.findDuplicates(arr)
    print(f"The answer is:{result_arr}")
    
