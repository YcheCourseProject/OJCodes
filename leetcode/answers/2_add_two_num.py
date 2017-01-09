class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = list()
        add_digit = 0

        iter_l1 = l1
        iter_l2 = l2
        while iter_l1 is not None or iter_l2 is not None:
            cur_sum = add_digit
            if iter_l1 is not None:
                cur_sum += iter_l1.val
            if iter_l2 is not None:
                cur_sum += iter_l2.val

            cur_digit = cur_sum % 10
            add_digit = cur_sum / 10
            l3.append(cur_digit)

            if iter_l1 is not None:
                iter_l1 = iter_l1.next
            if iter_l2 is not None:
                iter_l2 = iter_l2.next

        if add_digit != 0:
            l3.append(add_digit)
        return Solution.generate_list(l3)

    @staticmethod
    def generate_list(your_list):
        my_list = map(lambda ele: ListNode(ele), your_list)
        for i in xrange(len(my_list) - 1):
            my_list[i].next = my_list[i + 1]
        return my_list[0]


def generate_list(your_list):
    my_list = map(lambda ele: ListNode(ele), your_list)
    for i in xrange(len(my_list) - 1):
        my_list[i].next = my_list[i + 1]
    return my_list[0]


def loop_list(your_linked_list):
    my_iter = your_linked_list
    ret_list = []
    while my_iter is not None:
        ret_list.append(my_iter.val)
        my_iter = my_iter.next
    return ret_list


if __name__ == '__main__':
    l1 = generate_list([0])
    l2 = generate_list([7, 3])
    print loop_list(l1)
    print loop_list(l2)
    print loop_list(Solution().addTwoNumbers(l1, l2))
