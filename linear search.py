'''linearch'''
def linear_search(a,n):
    for i in range (len(a)):
        if(a[i]==n):
            return i
    return -1
a=[1,2,3,4,5]
n=3
re=linear_search(a, n)
if(re==0):
    print("number is not founded")
else:
    print("number is founded at position",str(re))