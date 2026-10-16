nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 10

newlst=[]

final=[]

if k<len(nums):
    for i in range(-k,0,1):
        newlst.append(nums[i])

    for i in range(len(nums)-k):
        final.append(nums[i])

    print(newlst+final)

