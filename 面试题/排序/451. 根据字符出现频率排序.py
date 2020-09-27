class Solution:
    def frequencySort(self, s: str) -> str:
        dic=dict(Counter(s))
        print(dic)
        l1=['' for e in range(len(s)+1)]
        for key,value in dic.items():
            l1[value]+=key*value
        print(l1)
        res=''
        for i in range(len(l1)-1,-1,-1):
            if l1[i]!='':
                res+=l1[i]
        return res

