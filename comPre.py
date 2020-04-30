class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        s1 = min(strs)
        s2 = max(strs)
        for i,j in  enumerate(s1):
            if j != s2[i]:
                return s1[:i]
        return s1
if __name__ == '__main__':
    s=Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))