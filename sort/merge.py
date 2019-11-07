import copy
from .data import Data


def split_merge(ds, head, tail, frame):
    mid = (head + tail) // 2  # floor division

    if tail - head > 2:
        split_merge(ds, head, mid, frame)
        split_merge(ds, mid, tail, frame)

    temp = copy.deepcopy(ds)

    for i in range(head, mid):
        temp[i].set_color('m')
    for i in range(mid, tail):
        temp[i].set_color('xkcd:sky blue')

    left = head
    right = mid

    temp_list = []

    for i in range(head, tail):
        frame.append(copy.deepcopy(temp))
        if right == tail or (left < mid and ds[left].value <= ds[right].value):
            temp_list.append(ds[left])
            frame[-1][left].set_color('r')
            left += 1

        else:
            temp_list.append(ds[right])
            frame[-1][right].set_color('r')
            right += 1

    for i in range(head, tail):
        ds[i] = temp_list[i - head]

    frame.append(copy.deepcopy(ds))


def merge_sort(data_set):

    frame = [data_set]

    ds = copy.deepcopy(data_set)

    split_merge(ds, 0, Data.data_count, frame)

    frame.append(ds)

    return frame
