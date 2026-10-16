nums = [12, 45, 2, 89, 7, 2, 90, 10]
sorted_lst=[]
for i in nums:
    if i not in sorted_lst:
        sorted_lst.append(i)

smallest_number=0
second_smallest_number=0
for i in sorted_lst:
    if smallest_number==0:
        smallest_number=i
    else:
        if i>smallest_number:
            continue
        else:
            smallest_number=i
print(smallest_number)
        
for i in sorted_lst:
    if i ==smallest_number:
        sorted_lst.remove(i)

for i in sorted_lst:
    if second_smallest_number==0:
        second_smallest_number=i
    else:
        if i>second_smallest_number:
            continue
        else:
            second_smallest_number=i
        
print(second_smallest_number)


    



