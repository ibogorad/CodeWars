def relatively_prime (n, l):
    # list_of_numbers = []
    # for i in l:
    #     if n%i !=0:
    #         list_of_numbers.append(i)
    # return list_of_numbers
    # factors of n
    # all_numbers_in_n = range(n)
    i = 2
    factors = []
    while i*i <= n:
        if n %i != 0:
            i+=1
        else:
            n//=i
            factors.append(i)
    if n > 1:
        factors.append(n)
    print set(factors)
print relatively_prime(888, [1,2,3,4,5,6,7])
# assert_equals(relatively_prime(8, [1,2,3,4,5,6,7]), [1,3,5,7])
# assert_equals(relatively_prime(15, [72,27,32,61,77,11,40]), [32, 61, 77, 11])
# assert_equals(relatively_prime(210, [15,100,2222222,6,4,12369,99]), [])
