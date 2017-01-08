def k_th_element(num_list, k):
    if k < 0 or k >= len(num_list):
        return None
    else:
        return k_th_element_detail(num_list, 0, len(num_list), k)


def k_th_element_detail(num_list, begin, end, k):
    if end - begin <= 0:
        return
    else:
        pivot_idx = end - 1
        left_idx, right_idx = begin, pivot_idx - 1
        while True:
            while num_list[left_idx] < num_list[pivot_idx] and left_idx <= right_idx:
                left_idx += 1
            while num_list[right_idx] > num_list[pivot_idx] and right_idx >= left_idx:
                right_idx -= 1

            if left_idx < right_idx:
                num_list[left_idx], num_list[right_idx] = num_list[right_idx], num_list[left_idx]
            else:
                num_list[pivot_idx], num_list[left_idx] = num_list[left_idx], num_list[pivot_idx]
                k_th_element_detail(num_list, begin, left_idx)
                k_th_element_detail(num_list, left_idx + 1, end)
                return
