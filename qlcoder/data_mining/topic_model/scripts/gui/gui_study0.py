# coding:utf-8
from ScrolledText import ScrolledText
from Tkinter import *

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


class App0:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.text_key_words = ScrolledText(frame)
        self.text_key_words.pack(side=LEFT)

        self.text_whole_text = ScrolledText(frame)
        self.text_whole_text.pack(side=LEFT)

        self.radio_btn_lst = map(lambda ele: Radiobutton(frame, width=35, text=ele), qlcoder_dict)
        for ele in self.radio_btn_lst:
            ele.pack()

        self.btn_prev = Button(frame, text='上一题', command=self.say_hi)
        self.btn_prev.pack()

        self.btn_next = Button(frame, text='下一题', command=self.say_hi)
        self.btn_next.pack()

        self.button = Button(frame, text='退出', fg='red', command=frame.quit)
        self.button.pack()

    def say_hi(self):
        print END
        self.text_key_words.insert(END, 'Hello~')
        self.text_whole_text.insert(END, ''.join(['我' for i in range(1000)]))


win = Tk()
app = App0(win)
win.mainloop()
