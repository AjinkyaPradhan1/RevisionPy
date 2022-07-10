#  Print without duplicates


list1 = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,1,2,3,4,5,1,2,34,1,2,3,1,2,1]

for i in range(len(list1)):
    num = list1.count(i)
    
    if(num>1):
        print("Number of times list has {}: ".format(i),list1.count(i))
