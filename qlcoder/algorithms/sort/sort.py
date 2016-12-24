# coding:utf-8
from Base import *


# 所有自定义函数写在class内部
class Answer(Base):
    def solve(self, items):
        self.quick_sort(items)
        return items

    def partition(self, items, begin, end):
        pivot = begin
        for i in xrange(begin + 1, end + 1):
            if self.compare(items[i].id, items[begin].id + 1):
                pivot += 1
                items[i], items[pivot] = items[pivot], items[i]
        items[pivot], items[begin] = items[begin], items[pivot]
        return pivot

    def quick_sort(self, items, begin=0, end=None):
        if end is None:
            end = len(items) - 1
        if begin >= end:
            return
        pivot = self.partition(items, begin, end)
        self.quick_sort(items, begin, pivot - 1)
        self.quick_sort(items, pivot + 1, end)

    def solve2(self, items):
        return self.bubble_sort(items)

    def bubble_sort(self, items):
        size = len(items)
        for i in range(size):
            for j in range(i + 1, size):
                if not self.compare(items[i].id, items[j].id):
                    temp = items[i]
                    items[i] = items[j]
                    items[j] = temp
        return items


class Item:
    def __init__(self, id, pos):
        self.id, self.pos = id, pos

    def __str__(self):
        return str(self.id) + str(self.pos)


def test_quick_sort():
    my_arr = [2, 1, 3, 5, 4]
    pos = ['a', 'b', 'c', 'd', 'e']
    my_items = [Item(my_arr[i], pos[i]) for i in range(len(my_arr))]
    res = Answer().solve(my_items)
    print len(res)
    for i in range(len(res)):
        print res[i]


def test_bubble_sort():
    my_arr = [2, 1, 3, 5, 4]
    pos = ['a', 'b', 'c', 'd', 'e']
    my_items = [Item(my_arr[i], pos[i]) for i in range(len(my_arr))]
    res = Answer().solve2(my_items)
    print len(res)
    for i in range(len(res)):
        print res[i]


test_bubble_sort()
print '\n'
test_quick_sort()
