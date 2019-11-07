import copy
from .data import Data


def bubble_sort(data_set):

    frame = [data_set]

    ds = copy.deepcopy(data_set)

    for i in range(Data.data_count -1):
        flag = False

        for j in range(Data.data_count - i - 1):
            if ds[j].value > ds[j+1].value:
                ds[j], ds[j+1] = ds[j+1], ds[j]
                flag = True

            frame.append(copy.deepcopy(ds))
            frame[-1][j+1].set_color('r')

        if not flag:
            break

    frame.append(ds)
    return frame
