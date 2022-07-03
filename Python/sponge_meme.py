def sponge_meme(s):
    news = ""
    for i,l in enumerate(s.lower()):
        if i % 2 == 0:
            l = l.upper()
            news += l
        else:
            news += l
    return news

# You need to create a function that converts the input into this format, with the output being the same string expect there is a pattern of uppercase and lowercase letters.

# Example:

# input:  "stop Making spongebob Memes!"
# output: "StOp mAkInG SpOnGeBoB MeMeS!"