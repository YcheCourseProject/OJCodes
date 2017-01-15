import re


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip()
        reg_pat = re.compile(r'^[+-]?[0-9]+')
        res = re.findall(reg_pat, str)

        if len(res) > 0:
            int_val = int(res[0])
            if int_val < -2147483648:
                return -2147483648
            elif int_val > 2147483647:
                return 2147483647
            else:
                return int_val
        else:
            return 0


if __name__ == '__main__':
    print Solution().myAtoi(' +-232,1.dsa123')
