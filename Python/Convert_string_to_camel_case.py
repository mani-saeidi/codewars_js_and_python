def to_camel_case(text):
    s = text.replace('_','-')
    words_list = s.split('-')
    capitalized_list = [words_list[0]]
    for each_word in words_list[1:]:
        capitalized_list.append(each_word.title());
    return "".join(capitalized_list)
    
    