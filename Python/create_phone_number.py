def create_phone_number(n):
    phone_num = '(xxx) xxx-xxxx'
    for each_number in n:
        phone_num = phone_num.replace("x",str(each_number),1)
    return phone_num
    