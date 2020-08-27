class Solution:
    def reOrderArray(self, array):
        tmp1=[]
        tmp2=[]
        for num in array:
            if num%2==0:
                tmp2.append(num)
            else:
                tmp1.append(num)

        for i in range(len(tmp1)):
            array[i]=tmp1[i]
        for j in range(len(tmp1),len(tmp1)+len(tmp2)):
            array[j]=tmp2[j-len(tmp1)]
        return array


