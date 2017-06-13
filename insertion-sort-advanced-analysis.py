# NOTE: this is not my code. I stole everything below.
#       I only slightly optimized mergesort; I added local variables to hold the value of len(ar) to reduce recomputation

def mergesort(ar, length):
    ic=0
    if length>1:
        mid=len(ar)//2
        left,right=ar[:mid],ar[mid:]
        length_left = mid
        length_right = length - mid
        ic+=mergesort(left, length_left)
        ic+=mergesort(right, length_right)
        i=j=k=0
        while i<length_left and j<length_right:
            if left[i]<=right[j]:
                ar[k]=left[i]
                i+=1
            else:
                ar[k]=right[j]
                j+=1
                ic+=mid-i
            k+=1
        while i<length_left:
            ar[k]=left[i]
            i+=1
            k+=1
        while j<length_right:
            ar[k]=right[j]
            j+=1
            k+=1
    return ic
# n = int(input())
# for iterate in range( n ):
#     size = int(input())
#     a = [ int( i ) for i in input().strip().split() ]
#     answer = mergesort(a, size)
#     # Write code to compute answer using x, a and answer
#     print(answer)


import random
list0 = random.sample(range(10000000), 100000)
list2 = [2,1,3,1,2]
list3 = [6,5,3,1,8,7,2,4]
lst = list3
print(mergesort(lst, len(lst)))
