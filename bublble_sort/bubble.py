def swap(a, b):
    temp = a
    a = b
    b = temp

    return a, b

def bubble(num, count):
    for a in range(0, count):
	print num[a]
        if num[a] > num[a+1]:
	    swap(num[a], num[a+1])

    return num, count 

bubble([1, 3, 10, 9, 6, 2, 4, 7, 5, 8], 9)
