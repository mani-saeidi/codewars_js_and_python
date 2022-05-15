def dont_give_me_five(start,end):
    nums_without_five = []
    for each_num in range(start,end+1):
        if str(5) not in str(each_num):
            nums_without_five.append(each_num)
    n = len(nums_without_five)
    return n