class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #归并排序
        tmp=[]
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                tmp.append(nums1[i])
                i=i+1
            elif nums1[i]>nums2[j]:
                tmp.append(nums2[j])
                j=j+1
            else:
                tmp.append(nums1[i])
                tmp.append(nums2[j])
                i=i+1
                j=j+1
        while i<len(nums1):
            tmp.append(nums1[i])
            i=i+1
        while j<len(nums2):
            tmp.append(nums2[j])
            j=j+1

        if len(tmp)%2==1:
            a =len(tmp)+1
            mm=tmp[int(a/2)-1]
            return mm
        else:
            return (tmp[int(len(tmp)/2)-1]+ tmp[int(len(tmp)/2)])/2