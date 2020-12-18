# Insertion Sort
A = [5,2,4,6,1,3]
n=len(A)

for j in range(1,n):
    key = A[j]
    i=j-1
    while i>=0 and A[i]>key:
        A[i+1]=A[i]
        i=i-1
    A[i+1]=key
    
print('Sorted seq:',A)