def increment_string(strng):
    head = strng.rstrip('0123456789')
    if head == strng:
        return head + str(1)
    tail = strng[len(head):]
    if len(tail) == len(str(int(tail))):
        return head + str(int(tail) + 1)
    tailhead = tail.rstrip('123456789')
    tailtail = tail[len(tailhead):]
    if len(tailtail) == 0:
        return head + str(0)*(len(tailhead)-1) + str(1)
    if len(str(int(tailtail) + 1))  == len(tailtail):
        return head + tailhead + str((int(tailtail)+1))
    else:
        return head + str(0)*(len(tailhead)-1) + str(int(tailtail)+1)

# Your job is to write a function which increments a string, to create a new string.

# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# Examples:

# foo -> foo1

# foobar23 -> foobar24

# foo0042 -> foo0043

# foo9 -> foo10

# foo099 -> foo100

# Attention: If the number has leading zeros the amount of digits should be considered.