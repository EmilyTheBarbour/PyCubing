def bubble_sort(self, list):
    for passnum in range(len(list) - 1, 0, -1):
        for i in range(passnum):
            if list[i] > list[i + 1]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
    return list
