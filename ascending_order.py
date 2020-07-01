def ascend_numbers(numbers,acsend_num):
    min_num=numbers[0]
    for i in range(0,len(numbers)):
        if (numbers[i]<min_num):
            min_num=numbers[i]
    acsend_num.append(min_num)
    numbers.remove(min_num)
    if(len(numbers)>0):
        ascend_numbers(numbers,acsend_num)
    return acsend_num

acsend_num=[]
numbers=[16,4,32,-10]
ascend_numbers(numbers,acsend_num)
print(acsend_num)
