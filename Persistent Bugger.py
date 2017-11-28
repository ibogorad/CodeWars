counter = 0
def persistence(n):
    global counter
    if n//10 == 0:
        answer = counter
        counter = 0
        return answer
    else:
        num_str = str(n)
        counter +=1
        return persistence(int(reduce(lambda x,y: int(x)*int(y), num_str)))

print persistence(39)
print persistence(4)