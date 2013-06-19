def quick():
    a = 0
    count = input('input number which input in list.')
    num = []

    while a < count:
        x = input('input list.')
        num.append(x)
        a = a + 1

    pivot = 0
    i = count-1
    while pivot < 1 and pivot is not i:
        if num[pivot] > num[pivot+1]:
            temp = num[pivot]
            num[pivot] = num[i]
            num[i] = temp

            i = i - 1
        else:
            pivot = pivot+1

    while pivot > 0 and pivot is not i:
        if num[pivot-1] < num[pivot] and num[pivot+1] < num[pivot]:
            temp = num[pivot]
            num[pivot] = num[i]
            num[i] = temp

            i = i - 1
            
        else:
            pivot = pivot+1

    print num

quick()
