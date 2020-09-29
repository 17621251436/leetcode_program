class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        count=0
        for i in words:
            num=0
            pos=-1
            for j in i:
                pos=S.find(j,pos+1)
                if pos==-1:
                    break
                else:
                    num=num+1
            if num==len(i):
                count=count+1
        return count

    