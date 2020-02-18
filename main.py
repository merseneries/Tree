import os
import json
from colored import fore, back, style

current_dir = r"E:\PycharmProjects\TestBad\resources"


def loop_tree(cur_dir):
    folder_list = []
    file_list = []
    dir_list = os.listdir(cur_dir)
    tmp = []

    for i in dir_list:
        current = os.path.join(cur_dir, i)
        if os.path.isdir(current):
            folder_list.append(i)
        else:
            file_list.append(i)

    if len(folder_list) != 0:
        for f in folder_list:
            tmp.append({f: loop_tree(os.path.join(cur_dir, f))})
    else:
        return file_list
    tmp.append(file_list)
    return tmp


def color_path(all_path):
    tmp = ""
    for one in all_path:
        if type(one) == dict:
            for k, v in one.items():
                tmp += fore.SPRING_GREEN_4 + style.BOLD + k + "\n"
                tmp += color_path(v)
        elif type(one) == list:
            tmp += color_path(one)
        else:
            tmp += fore.LIGHT_YELLOW + one + "\n"
    return tmp


path = loop_tree(current_dir)
path = color_path(path)
