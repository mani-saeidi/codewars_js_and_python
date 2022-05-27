def unpack_sausages(truck):
    packaged_items = []
    for each_list in truck:
        for each_element in each_list:
            packaged_items.append(each_element)
    six_char_items = list(filter(lambda el: len(el) == 6, packaged_items))
    sausages_only = list(filter(lambda el: el[0]=='[' and el[1] == el[2] and el[2] == el[3] and el[3]==el[4] and el[5]==']', six_char_items))
    customer_sausages_only_grouped = [el for index,el in enumerate(sausages_only) if ((index+1) % 5)!=0]
    customer_sausages_only = list(map(lambda el: el[1:5],customer_sausages_only_grouped))
    customer_sausages = []
    for each_group in customer_sausages_only:
        customer_sausages.append([j for i,j in enumerate(each_group)])
    individual_sausages = []
    for each_list in customer_sausages:
        if each_list is not customer_sausages[len(customer_sausages)-1]:
            individual_sausages.append(each_list[0] + ' ' + each_list[1] + ' ' + each_list[2] + ' ' + each_list[3] + ' ')
        else:
            individual_sausages.append(each_list[0] + ' ' + each_list[1] + ' ' + each_list[2] + ' ' + each_list[3])
    return ''.join(individual_sausages)
    
# Unpack delicious sausages!
# A food delivery truck carrying boxes of delicious sausages has arrived and it's your job to unpack them and put them in the store's display counter.

# The truck is filled with boxes of goods. Among the goods, there are various types of sausages. Straight sausages I, curvy sausages ), even twirly sausages @ and many more. The safest way to tell any type of sausage apart from other goods is by the packaging [], used exclusively by sausages. Make sure to ignore other goods, those will be taken care of by someone else. Once you have unpacked all the sausages, just lay them out in the display counter (string) in the same order in which they came in boxes with one space " " in-between every sausage. Oh, and watch out for spoiled or damaged sausage packs, did I tell you about those? The sausages are always packed in fours and each pack contains only one sausage type, so whenever there is any irregularity, the sausages are probably spoiled or damaged and the whole pack should be thrown out!

# Now we're getting to the best part - your reward! Instead of money, you'll be paid in something far better - sausages! Every fifth undamaged processed pack of sausages doesn't go to the counter, instead it's yours to keep. Don't go spending it all at once!

# If the truck arrives completely empty, only with empty boxes or only with goods that are not sausages, the display counter will simply stay empty "". Unlike truck and boxes that may be empty, every existing product is a non-empty string.

# Example:
# Input (truck with 5 boxes containing 11 products):

# [("(-)", "[IIII]", "[))))]"), ("IuI", "[llll]"), ("[@@@@]", "UwU", "[IlII]"), ("IuI", "[))))]", "x"), ()]

# "Truck is a list, boxes are tuples, packages of goods are strings"
# Output (four sets of sausages):

# "I I I I ) ) ) ) l l l l @ @ @ @"

# Explanation:

# The last box is empty and is therefore ignored
# Packages with products that are not sausages are ignored - "(-)", "IuI", "UwU", "IuI", "x"
# One damaged package gets thrown out - "[IlII]"
# Fifth undamaged package is used as your reward and is therefore excluded from the output: "[))))]"
# More examples of input and expected output can be seen in the example test cases