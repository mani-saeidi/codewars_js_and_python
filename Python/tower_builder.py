def tower_builder(n_floors):
    max_stars = 2*n_floors-1
    list = []
    for n in range(1,max_stars+1,2):
        list.append((" "*int((max_stars-n)/2)) + (("*")*n) + (" "*int((max_stars-n)/2)))
    return list

# Build Tower
# Build a pyramid-shaped tower given a positive integer number of floors. A tower block is represented with "*" character.

# For example, a tower with 3 floors looks like this:

# [
#   "  *  ",
#   " *** ", 
#   "*****"
# ]
# And a tower with 6 floors looks like this:

# [
#   "     *     ", 
#   "    ***    ", 
#   "   *****   ", 
#   "  *******  ", 
#   " ********* ", 
#   "***********"
# ]