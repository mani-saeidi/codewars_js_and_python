def to_weird_case(string):
    word_list = string.split(' ')
    weird_list = []
    for each_word in word_list.copy():
        weird_word = ""
        for index, each_letter in enumerate(each_word):
            if index % 2 == 0: 
                weird_word += each_letter.upper()
            else:
                weird_word += each_letter
        print(weird_word)
        weird_list.append(weird_word)
    return ' '.join(weird_list)
    
print(to_weird_case('This is a test'))
# ThIs Is A TeSt