x=[8,3,12.5,45,25.5,52,1]
y=[]
i=0
b=min(x)
while i<7:
    if x[i]!=b:
        continue
    else:
        y.append(x[i])
    i=i+1
    print(y[i])
