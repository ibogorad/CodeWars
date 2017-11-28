def accum(s):
    # your code
    mylist = []
    for i in range(len(s)):
        if i == 0:
            mylist.append(s[i].upper())
        if i >0:
            mylist.append((s[i].upper())+(i)*s[i].lower())
    final = mylist[0]
    for i in mylist[1::]:
        final = final + "-" + i
    return final
accum("ZpglnRxqenU")
