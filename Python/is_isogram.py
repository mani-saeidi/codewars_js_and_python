def is_isogram(string):
    isogram = {}
    for i in string.lower():
        isogram[i] = isogram.get(i,0)+1
    for key in isogram:
        if isogram[key] > 1:
            return False
    return True

# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# Example: (Input --> Output)

# "Dermatoglyphics" --> true
# "aba" --> false
# "moOse" --> false (ignore letter case)