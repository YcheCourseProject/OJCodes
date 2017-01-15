class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_ch = None
        expand_list = []
        for i, ch in enumerate(s):
            expand_list.append((i, i + 1))
            if ch == last_ch:
                expand_list.append((i - 1, i + 1))
            last_ch = ch
        print expand_list


if __name__ == '__main__':
    input_str = 'babad'
    print Solution().longestPalindrome(input_str)
    input_str = 'cbbd'
    print Solution().longestPalindrome(input_str)
