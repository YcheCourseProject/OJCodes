# coding:utf-8
from ScrolledText import ScrolledText
import Tkinter as tk
import operator

qlcoder_dict = {
    'IT': 1,
    '健康': 2,
    '体育': 3,
    '旅游': 4,
    '教育': 5,
    '文化': 6,
    '军事': 7,
    '财经': 8

}

category_list = ['IT', '健康', '体育', '旅游', '教育', '文化', '军事', '财经']


def get_frequency_dict(words):
    frequency_dict = dict()
    for word in words:
        if word not in frequency_dict:
            frequency_dict[word] = 0
        frequency_dict[word] += 1

    sorted_x = sorted(frequency_dict.items(), key=operator.itemgetter(1))[::-1]
    return map(lambda ele: ele[0], sorted_x)


def get_word_list():
    word_list = []
    for i in range(8000):
        with open('../../8000_words/' + str(i) + '.txt') as ifs:
            lines = ifs.readlines()
            lines = map(lambda line: line.strip(), lines)
            word_list.append(get_frequency_dict(lines))
    return word_list


def get_text_list():
    text_list = []
    for i in range(8000):
        with open('../../8000_copy/' + str(i) + '.txt') as ifs:
            lines = ifs.readlines()
            text_list.append(''.join(lines))
    return text_list


class App0:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()

        self.question_idx = 0
        self.word_list = get_word_list()
        self.text_list = get_text_list()
        self.count = 0

        self.text_key_words = ScrolledText(frame)
        self.text_key_words.pack(side=tk.LEFT)

        self.text_whole_text = ScrolledText(frame)
        self.text_whole_text.pack(side=tk.LEFT)

        self.category_btn_var = tk.IntVar()
        self.radio_btn_lst = map(
            lambda ele: tk.Radiobutton(frame, width=25, height=3, text=ele, variable=self.category_btn_var,
                                       value=qlcoder_dict[ele], command=self.select_callback(ele)), category_list)
        for ele in self.radio_btn_lst:
            ele.pack()

        tag_id = 2
        self.radio_btn_lst[tag_id - 1].select()

        self.btn_prev = tk.Button(frame, text='上一题', height=2, command=self.question_callback('prev'))
        self.btn_prev.pack()
        self.btn_next = tk.Button(frame, text='下一题', height=2, command=self.question_callback('next'))
        self.btn_next.pack()

        self.button = tk.Button(frame, text='退出', height=2, fg='red', command=frame.quit)
        self.button.pack()

    def select_callback(self, ele):
        def test():
            print 'test' + str(ele)
            print 'var:' + str(self.category_btn_var.get())

        return test

    def question_callback(self, indicate_str):
        def say_hi():
            if indicate_str == 'prev':
                self.question_idx += 8000 - 1
            elif indicate_str == 'next':
                self.question_idx += 1
            else:
                print 'error'
            self.question_idx %= 8000

            self.count += 1
            print indicate_str, self.count
            self.text_key_words.delete(1.0, tk.END)
            self.text_key_words.insert(tk.END, ','.join(self.word_list[self.question_idx]))
            self.text_whole_text.delete(1.0, tk.END)
            self.text_whole_text.insert(tk.END, ''.join(self.text_list[self.question_idx]))

        return say_hi


win = tk.Tk()
win.title('topic model human helper')
app = App0(win)
win.mainloop()
