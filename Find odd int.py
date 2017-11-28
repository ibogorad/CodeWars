def find_it(seq):
    mydict = {}
    for i in seq:
        if i not in mydict:
            mydict[i] = 1
        else:
            mydict[i] += 1
    for i in mydict:
        if mydict[i]%2!=0:
            print i
            return i
find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])
