def ips_between(start, end):
    ipone = start.split('.')
    iptwo = end.split('.')
    ipdiff = []
    for ind, each_number in enumerate(ipone):
        for index, each_num in enumerate(iptwo):
            if ind == index:
                 ipdiff.append(int(each_num) - int(each_number))
    
    return ipdiff[0]*256*256*256 + ipdiff[1]*256*256 + ipdiff[2]*256 + ipdiff[3]
    
print(ips_between("20.0.0.10", "20.0.1.0"))

# Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

# All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

# Examples
# * With input "10.0.0.0", "10.0.0.50"  => return   50 
# * With input "10.0.0.0", "10.0.1.0"   => return  256 
# * With input "20.0.0.10", "20.0.1.0"  => return  246