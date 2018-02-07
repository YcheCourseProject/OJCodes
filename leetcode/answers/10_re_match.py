class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        def is_match_detail(s_beg, s_len, p_beg, p_len):
            # bottom condition
            if s_len == 0 and p_len == 0:
                return True
            if s_len == 0:
                if p_len % 2 != 0:
                    return False
                for i in xrange(1 + p_beg, p_len + p_beg, 2):
                    if p[i] != '*':
                        return False
                return True
            if s_len != 0 and p_len == 0:
                return False

            # 1st: expand for '*', one-hop expansion
            if p_len >= 2:
                if p[p_beg + 1] == '*':
                    return is_match_detail(s_beg, s_len, p_beg + 2, p_len - 2) or \
                           (is_match_detail(s_beg + 1, s_len - 1, p_beg, p_len)
                           if p[p_beg] == '.' or p[p_beg] == s[s_beg] else False)

            # 2nd: for others
            if p[p_beg] == '.' or p[p_beg] == s[s_beg]:
                return is_match_detail(s_beg + 1, s_len - 1, p_beg + 1, p_len - 1)

            # 3rd: not match here
            return False

        return is_match_detail(0, len(s), 0, len(p))


if __name__ == '__main__':
    print Solution().isMatch('aa', 'a')
    print Solution().isMatch("aa", "a")
    print Solution().isMatch("aa", "aa")
    print Solution().isMatch("aaa", "aa")
    print Solution().isMatch("aa", "a*")
    print Solution().isMatch("aa", ".*")
    print Solution().isMatch("ab", ".*")
    print Solution().isMatch("aab", "c*a*b")

    print Solution().isMatch("a", ".*..a*")
