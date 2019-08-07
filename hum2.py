element=[5,1,1,2,5,6,3,4,4,4,2]
li=[]
gi=[]
for nombre in element:
    if li.count(nombre)>=1:
        continue
    else:
        li.append(nombre)
while li:
    mini=li[0]
    for x in li:
        if x<mini:
            mini=x
    gi.append(mini)
    li.remove(mini)
print(gi)


    

