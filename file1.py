# li = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]
#
#
# for i in range(len(li)):
n=int(input("enter the number-->"))
count=1
for i in range(n):
    for j in range(i+1):
        if count<=9:
            print("0"+str(count) ,end=" ")
            count+=2
        else:
            print( str(count), end=" ")
            count += 2
    print()

