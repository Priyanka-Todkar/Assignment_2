# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


inputlist = []
list_max=int(input("enter number of sets in list: "))
for i in range(list_max):
    print(f"enter details of {i+1} tuple")
    firstint=int(input ("Enter the first value "))
    secondint=int(input ("Enter the second value "))
    inputlist.append((firstint,secondint))
print(inputlist)

for i in range(1,len(inputlist)):
    curtuple=inputlist[i]
    j=i-1
    while curtuple[1]<inputlist[j][1] and j >=0:
        inputlist[j+1]=inputlist[j]
        j-=1
    inputlist[j+1]=curtuple
print(inputlist)