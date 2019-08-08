with open("notes.txt","r")as notes , open("notes2.txt","w") as notes2:
    lignes=notes.readlines()
    mate=[]
    i=0
    while i<len(lignes):
       mate=mate+[float(lignes[i])]
       i=i+1
    for elt in mate:
        if elt >=10:
            notes2.write( "{:.1f} admis\n".format(elt))
        else:
            notes2.write("{:.1f} relalé\n".format(elt))
            
