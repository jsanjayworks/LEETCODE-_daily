class Solution(object):
    def search(self, nums, target):
      l=0
      r=len(nums)-1
      mid=(l+r)//2
      while l<=r:
        mid=(l+r)//2
        if nums[mid]==target:
            return mid 
        elif nums[mid]>target:
            r=mid-1
        
        elif nums[mid]<target:
            l=mid+1
      return -1

            