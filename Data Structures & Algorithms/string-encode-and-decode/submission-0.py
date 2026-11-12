class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=[]
        for i in strs:
            ans.append(f"{len(i)}#{i}")
        return "".join(ans)
    def decode(self, s: str) -> List[str]:
        ans=[]
        j= 0
        while j <len(s):
            i=j   
            while s[j] != "#":
                j+=1
             
            length =int(s[i:j])
            strt = j+1
            end=strt + length
            ans.append(s[strt:end])
            j = end
        return ans





        
