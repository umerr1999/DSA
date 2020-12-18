A=[98,23,45,14,6,67,33,42]
n = len(A)
for i in range(n-1):
    flag=False
    for j in range(n-i-1):
        if A[j]>A[j+1]:
            A[j],A[j+1]=A[j+1],A[j]
            flag=True
    if flag != True:
        break
            
print('The sorted list is',A)

