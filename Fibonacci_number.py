def fibonacci_number(n):
    list_num = [1,1]

    for i in range(n - 2):
        k = len(list_num) - 1
        new_num = list_num[k - 1] + list_num[k]
        list_num.append(new_num)

    print(list_num)


fibonacci_number(50)
