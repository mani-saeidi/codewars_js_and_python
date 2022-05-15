def move_zeros(array):
    for each_num in array:
        if each_num == 0:
            removed_zero = array.remove(each_num)
            array.append(0)
    return array