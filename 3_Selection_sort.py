def SelectionSort(arr):
    for i in range(len(arr)):
        min=float('-inf')
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
                
    return arr
print("The array after sorting in ascending order by using selection sort:")
print(SelectionSort([3,7,5,2,6,1]))