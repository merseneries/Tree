import os
import json

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
    print(json.dumps(tmp,indent=4))


loop_tree(current_dir)
