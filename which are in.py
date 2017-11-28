def in_array(array1, array2):
    mylist = []
    for i in array1:
        for j in array2:
            if i in j:
                mylist.append(i)
    return sorted(list(set(mylist)))
a1 = ["live", "arp", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = ['arp', 'live', 'strong']
print in_array(a1, a2)