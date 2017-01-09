class Solution(object):
    def __init__(self):
        self.max_len = 0
        self.max_len_sub_str = None

        self.idx_dict = dict()
        self.begin_idx = 0
        self.end_idx = 0

    def update_dict_and_range(self, s, idx, is_last=False):
        self.end_idx = idx
        if self.end_idx - self.begin_idx > self.max_len:
            self.max_len = self.end_idx - self.begin_idx
            self.max_len_sub_str = s[self.begin_idx:self.end_idx]

        if not is_last:
            repeat_ele_idx = self.idx_dict[s[idx]]
            for i in range(self.begin_idx, repeat_ele_idx + 1):
                self.idx_dict.pop(s[i])
            self.begin_idx = repeat_ele_idx + 1

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.__init__()
        for idx, my_ch in enumerate(s):
            if my_ch in self.idx_dict:
                self.update_dict_and_range(s, idx)
            self.idx_dict[my_ch] = idx
        self.update_dict_and_range(s, len(s), True)
        return self.max_len


if __name__ == '__main__':
    sol = Solution()
    print sol.lengthOfLongestSubstring('abcabcbb')
    print sol.lengthOfLongestSubstring('bbbbbacd')
    print sol.lengthOfLongestSubstring('pwwkew')
