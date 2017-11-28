def digital_root(n):
    if n//10 == 0:
        return n
    else:
        num_str = str(n)
        return digital_root(reduce(lambda x,y: int(x)+int(y),num_str))