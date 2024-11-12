def Right_Rotation(arr,k):
    n=len(arr)
    k=int(k%n)
    a=arr[-k:]+arr[:-k]
    return a 
arr=[1,2,3,4,5,6,7]
k=3
print(Right_Rotation(arr,k))   
