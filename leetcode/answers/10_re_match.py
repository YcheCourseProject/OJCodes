class Solution(object):
    @staticmethod
    def get_star_pos(pat_str):
        ret = []
        for idx, ele in enumerate(pat_str):
            if ele == '*':
                ret.append((idx - 1, idx + 1))
        return ret

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        print Solution.get_star_pos(p)


if __name__ == '__main__':
    Solution().isMatch('aa', 'a')
    Solution().isMatch("aa", "a")
    Solution().isMatch("aa", "aa")
    Solution().isMatch("aaa", "aa")
    Solution().isMatch("aa", "a*")
    Solution().isMatch("aa", ".*")
    Solution().isMatch("ab", ".*")
    Solution().isMatch("aab", "c*a*b")
