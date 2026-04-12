class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #Horizontal Scanning
        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1] # shrink the prefix to get exact match
                if not prefix:
                    return ""

        return prefix


        