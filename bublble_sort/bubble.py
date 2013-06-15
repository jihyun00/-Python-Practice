def bubble():
    num = []
    a = 0
    y = 0
    count = input('input number which input in list')
    
    while y < count:
        x = input('input list.')
        num.append(x)
	y = y+1

    while count>0:
        for i in range(count):
	    if i+1 < count:
                if num[i] > num[i+1]:
	            temp = num[i+1]
		    num[i+1] = num[i]
		    num[i] = temp
        count = count-1

    print num

    return

bubble()

