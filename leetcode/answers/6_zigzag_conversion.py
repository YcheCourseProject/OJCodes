class Solution(object):
    @staticmethod
    def get_row_col(idx, row_offset_list, col_offset_list):
        col_size = col_offset_list[-1] + 1
        col = col_size * (idx / len(col_offset_list)) + col_offset_list[idx % len(col_offset_list)]
        row = row_offset_list[idx % len(col_offset_list)]
        return row, col

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        else:
            col_offset_list = tuple(0 if i < numRows else i - numRows + 1 for i in range(numRows * 2 - 2))
            row_offset_list = tuple(i if i < numRows else 2 * (numRows - 1) - i for i in range(numRows * 2 - 2))
            return ''.join(map(lambda my_ele: my_ele[1],
                               sorted(map(lambda ele: (
                                   ele[0], ele[1], Solution.get_row_col(ele[0], row_offset_list, col_offset_list)),
                                          enumerate(s)), key=lambda x: x[2])))


if __name__ == '__main__':
    print Solution().convert('PAYPALISHIRING', 4)
    print 'PINALSIGYAHRPI'
