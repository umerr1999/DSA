#SELECTION SORT

A = [8,4,6,9,7,2,3,7,1]
n = len(A)

for j in range(n-1):
    smallest = j
    for i in range(j+1,n):
        if A[i]<A[smallest]:
            smallest = i
    # Now exchange A[j] with A[smallest]
    A[j],A[smallest]=A[smallest],A[j]
    
    
print('Sorted list is: ',A)