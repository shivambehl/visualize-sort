import random
import matplotlib.pyplot as plt
from matplotlib import animation
from sort.data import Data
from sort.bubble import bubble_sort
from sort.merge import merge_sort
from sort.insertion import insertion_sort

plt.style.use('fivethirtyeight')

function = [bubble_sort, insertion_sort, merge_sort]

titles = ['Bubble Sort', 'Insertion Sort', 'Merge Sort']

sort_menu = {'bubble-sort': 0, 'insertion-sort': 1, 'merge-sort': 2}


def create_data(data_type):
    data = []
    if data_type == 'random':
        data = list(range(1, Data.data_count+1))
        random.shuffle(data)
    elif data_type == 'reversed':
        data = list(range(Data.data_count+1, 1, -1))
    else:
        data = list(range(1, Data.data_count + 1))
        random.shuffle(data)
    return data


def draw_chart(sorting_type, original_data, frame_interval):
    # First set up the figure, the axis, and the plot elements we want to animate.
    fig = plt.figure(1, figsize=(8, 4.5))
    data_set = [Data(d) for d in original_data]
    axs = fig.add_subplot(111)
    axs.set_xticks([])
    axs.set_yticks([])
    plt.subplots_adjust(left=0.01, bottom=0.01, right=0.99, top=0.9)

    frames = function[sorting_type](data_set)

    # print('%s: %d frames.' % (re.findall(r'\w+ Sort', titles[stype])[0], len(frames)))

    def animate(fi):
        bars = []
        if len(frames) > fi:
            axs.cla()
            axs.set_title(titles[sorting_type])
            axs.set_xticks([])
            axs.set_yticks([])
            bars += axs.bar(list(range(Data.data_count)),  # X
                            [d.value for d in frames[fi]],  # data
                            1,  # width
                            color=[d.color for d in frames[fi]]  # color
                            ).get_children()
        return bars

    # Call the animator.
    anim = animation.FuncAnimation(fig, animate, frames=len(frames), interval=frame_interval)
    plt.show()


if __name__ == "__main__":
    Data.data_count = 10
    data_type = 'random'  # can be random and reversed
    original_data = create_data(data_type)
    fps = 50
    sorting_type_str = 'insertion-sort'
    sorting_type = sort_menu[sorting_type_str]
    draw_chart(sorting_type, original_data, fps)





