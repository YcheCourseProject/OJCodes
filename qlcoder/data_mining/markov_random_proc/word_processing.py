class TextSolver:
    @staticmethod
    def get_text_strs():
        with open('word_processing_data.txt') as ifs:
            text_str = ifs.readline().strip()
        text_strs = text_str.split('1')
        print text_strs
        return text_strs

    @staticmethod
    def get_english_words():
        with open('word_list.txt') as fs:
            lines = fs.readlines()
            lines = map(lambda word: word[0: len(word) - 2], lines)
            lines = set(lines)
            return lines

    @staticmethod
    def get_key_board_dict():
        kb_mp = dict()
        kb_mp['2'] = ['q', 'b', 'x']
        kb_mp['3'] = ['z', 'u', 'v']
        kb_mp['4'] = ['g', 'h', 'j']
        kb_mp['5'] = ['m', 'p', 'l']
        kb_mp['6'] = ['f', 'c', 'y', 't']
        kb_mp['7'] = ['k', 'n', 'r']
        kb_mp['8'] = ['a', 'e', 'w']
        kb_mp['9'] = ['i', 'd', 'o', 's']
        return kb_mp

    def __init__(self):
        self.kb_mp = TextSolver.get_key_board_dict()
        self.english_words = TextSolver.get_english_words()
        self.kb_mp = TextSolver.get_key_board_dict()
        for text in TextSolver.get_text_strs():
            self.print_possibles(text)

    def dfs(self, my_str):
        if len(my_str) == 1:
            return self.kb_mp[my_str[0]]
        else:
            cur_ch = my_str[0]
            ret_res = []
            for ch in self.kb_mp[cur_ch]:
                tmp_res = map(lambda e: ch + e, self.dfs(my_str[1:len(my_str)]))
                ret_res.extend(tmp_res)
            return ret_res

    def print_possibles(self, my_str):
        if len(my_str) == 0:
            return
        else:
            print '-------------------------'
            tmp = []
            for ele in self.dfs(my_str):
                if self.english_words.__contains__(ele):
                    tmp.append(ele)
            if len(tmp) > 0:
                print ','.join(tmp)
            else:
                print ' or . or !'


if __name__ == '__main__':
    TextSolver()
