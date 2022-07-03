def pig_it(text):
    words = text.split(' ')
    new_text = ''
    for word in words:
        if word != '!' and word != ',' and word != ',' and word != '?':
            word += word[0] + "ay"
            word = word[1:] 
            new_text += word + ' ' 
        else: 
            word += word[0]
            word = word[1:] 
            new_text += word + ' '
    return new_text[0:-1]


# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !
