def pairSum(list, num):
    l = len(list)
    if(l < 2):
        return
    pair = [(x,y) for x in list for y in list if(x + y == num)]
    return pair
list = [3, 4, 5, 6, 9, 7, -6, -2, -1, 8]
num = 4
result = pairSum(list, num)
if(result == [] ):
    print("The set empty")
else:
    print("The List is:",result)
