class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        begin=0
        end=len(nums)-1
        nums=sorted(nums)
        tmp=[]
        for i in range(len(nums)-3):
            if i>0 and  nums[i]==nums[i-1]:
                continue
            if nums[i]+3*nums[i+1]>target:
                break
            if nums[i]+3*nums[-1]<target:
                continue

            for j in range(i+1,len(nums)-2):

                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                # 5) 剪枝第三处
                if nums[i]+nums[j]+2*nums[j+1] > target:
                    break
                # 6) 剪枝第四处
                if nums[i]+nums[j]+2*nums[-1] < target:
                    continue
                begin=j+1
                end =len(nums)-1
                while begin<end:
                    res= nums[begin]+nums[end]+nums[i]+nums[j]
                    if res==target:
                        tmp.append([nums[i],nums[j],nums[begin],nums[end]])

                        begin=begin+1
                        end=end-1
                        while begin<end and nums[begin]==nums[begin-1]:
                            begin=begin+1

                        while begin<end and nums[end]==nums[end+1]:
                            end=end-1

                    elif  res>target:
                        end=end-1
                    else:
                        begin =begin+1
        return tmp