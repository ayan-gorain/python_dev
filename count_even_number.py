def count_even(str):
    count = 0
    for i in  str :
        if i % 2 ==0:
            count+=1
    print(count)

count_even([1, 2, 3, 4, 6])