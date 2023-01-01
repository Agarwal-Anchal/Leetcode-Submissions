# class Solution:
#     def wordPattern(self, pattern: str, s: str) -> bool:
#         s=s.split()
#         if len(s)!=len(pattern): return False
#         memo={}
#         for idx,word in enumerate(s):
#             if (ord(pattern[idx])-97 in memo and memo[ord(pattern[idx])-97]!=word) or (word in memo and memo[word]!=ord(pattern[idx])-97):
#                     return False
#             memo[ord(pattern[idx])-97]=word
#             memo[word]=ord(pattern[idx])-97
#         return True
        
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        st=list(s.split(' '))

        vis1=set()
        vis2=set()
        c1=0
        c2=0
        pat1=[0]*len(pattern)
        pat2=[0]*len(st)

        for i in range(len(pattern)):
            if pattern[i] not in vis1:
                vis1.add(pattern[i])
                c1+=1
                pat1[i]=c1
            else:
                pat1[i]=pat1[pattern.index(pattern[i])]
        # print(pat1)
        for i in range(len(st)):
            if st[i] not in vis2:
                vis2.add(st[i])
                c2+=1
                pat2[i]=c2
            else:
                pat2[i]=pat2[st.index(st[i])]
        # print(pat2)
        return pat1==pat2
