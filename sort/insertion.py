import copy
from .data import Data


def insertion_sort(data_set):
    frame = [data_set]

    ds = copy.deepcopy(data_set)

    for i in range(1, Data.data_count):
        frame.append(copy.deepcopy(ds))
        frame[-1][i].set_color('r')
        for j in range(i, 0, -1):
            if ds[j].value < ds[j-1].value:
                ds[j], ds[j-1] = ds[j-1], ds[j]
                frame.append(copy.deepcopy(ds))
                frame[-1][j-1].set_color('r')

            else:
                break

    frame.append(ds)

    return frame