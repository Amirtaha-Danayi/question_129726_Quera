def separator(*ls):
    # list = []
    # list.append(ls)
    couples = []
    odd = []
    print(list)
    for i in ls:
        if i % 2 == 0:
            couples.append(i)
        else:
            odd.append(i)
    numbers = (couples, odd)
    return(numbers)
    
