test_range = int(input(""))
    
for i in range (1,test_range+1):
    arr_len = int(input(""))
    arr = input("").split()
    for i in range(0, len(arr)): 
        arr[i] = int(arr[i])
    arr2 = sorted(arr)

    if (arr==arr2):
        print ("1")
    else:
        print ("0")


