n=int(input("Give a number till you want the Fibonacci: "))
l=[0,  1]
i = 1
while i<n-1:     # i could be used as index
    s = l[i] + l[i-1]
    if i==1:
        i==2
    l.append(s)
    i=i+1

print(l)