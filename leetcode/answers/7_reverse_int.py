class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        my_str = str(x)
        if my_str[0] == '-':
            ret = -int(''.join(reversed(my_str[1:])))
        else:
            ret = int(''.join(reversed(my_str)))

        if abs(ret)> 0x7fffffff:
            return 0
        else:
            return ret

if __name__ == '__main__':
    print Solution().reverse(123)
    print Solution().reverse(-123)
    print Solution().reverse(1534236469)
