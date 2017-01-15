class Solution(object):
    @staticmethod
    def get_max_size(beg, end, s):
        return end - beg + 2 * min(beg, len(s) - end)

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_ch = None
        expand_list = [[] for i in range(len(s))]

        for i, ch in enumerate(s):
            expand_list[Solution.get_max_size(i, i + 1, s) - 1].append((i, i + 1))
            if ch == last_ch:
                expand_list[Solution.get_max_size(i - 1, i + 1, s) - 1].append((i - 1, i + 1))
            last_ch = ch

        cur_str_pair, cur_max_size = None, 0

        def expand_ele(ele):
            beg = ele[0]
            end = ele[1]
            while beg - 1 >= 0 and end < len(s):
                if s[beg - 1] == s[end]:
                    beg, end = beg - 1, end + 1
                else:
                    return (beg, end), end - beg

            return (beg, end), end - beg

        for i in xrange(len(s) - 1, -1, -1):
            if cur_max_size >= i + 1:
                break
            for ele in expand_list[i]:
                ele_iter_pair, exp_size = expand_ele(ele)
                if exp_size > cur_max_size:
                    cur_str_pair, cur_max_size = ele_iter_pair, exp_size

        return s[cur_str_pair[0]:cur_str_pair[1]]


if __name__ == '__main__':
    input_str = 'babad'
    print Solution().longestPalindrome(input_str)
    input_str = 'cbbd'
    print Solution().longestPalindrome(input_str)
    input_str = 'a'
    print Solution().longestPalindrome(input_str)

