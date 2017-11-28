def iq_test(numbers):
    num_list = map(int,numbers.split())
    newlist = []
    for i in num_list:
        newlist.append(i%2)
    if newlist.count(1) == 1:
        return newlist.index(1)+1
    else:
        return newlist.index(0)+1


print iq_test("2 4 7 8 10")