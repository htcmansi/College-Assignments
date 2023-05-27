def Selectionsort(arr):
    for i in range(len(arr)):
        min=float('-inf')
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
                
    return arr

print("Array in ascending order using selection sort:")
print(Selectionsort([9,5,6,7,2,1,8]))