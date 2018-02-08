class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        max_prefix_str = []
        first_str = strs[0]
        for round in xrange(min(map(len, strs))):
            first_ch = first_str[round]

            for i in xrange(1, len(strs)):
                if strs[i][round] != first_ch:
                    return ''.join(max_prefix_str)
            max_prefix_str.append(first_ch)
        return ''.join(max_prefix_str)


if __name__ == '__main__':
    print Solution().longestCommonPrefix([])
    print Solution().longestCommonPrefix(["a"])
    print Solution().longestCommonPrefix(["a", "ab"])
    print Solution().longestCommonPrefix(["ab", "ab", "abc"])
