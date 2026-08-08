class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        M,N=len(word1),len(word2)
        m,n=0,0
        word=1
        result=[]

        while m<M and n<N:
            if word==1:
                result.append(word1[m])
                m+=1
                word=2
            else:
                result.append(word2[n])
                n+=1
                word=1
        while m<M:
            result.append(word1[m])
            m+=1
        while n<N:
            result.append(word2[n])
            n+=1
        return ''.join(result)
