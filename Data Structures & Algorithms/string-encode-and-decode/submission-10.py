class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = []

        for s in strs:
            encoding.append(str(len(s)))
            encoding.append("#")
            encoding.append(s)

        return "".join(encoding)

        return encoding 

    def decode(self, s: str) -> List[str]:

        output = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            output.append(s[j+1:j+1+length])
            i = j+1+length
        
        return(output)
