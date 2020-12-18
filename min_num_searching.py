# Minimum Number Searching Algorithm
x = [6,5,8,6,3,8,0,1,3,6,-1,6,3]

smallest = x[0]

for i in range(1,len(x)):
    if x[i]<smallest:
        smallest = x[i]
        
print('smallest number is: ',smallest)
index = x.index(smallest)
print('index is: ', index)