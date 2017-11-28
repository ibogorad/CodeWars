def create_phone_number(n):
    str_list = "".join(str(i) for i in n)
    return "("+str_list[0:3]+") " + str_list[3:6]+"-"+str_list[6::]
print create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
