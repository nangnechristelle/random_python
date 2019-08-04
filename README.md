# random_python
a code to create a list from random choice of element of another list
import random as ran
def seq_alea(n):
   base=["A","C","T","G"]
   li=[]
   reponse=input('entrer un nombre')
   n=int(reponse)
   i=0
   while i<n:
       li.append(ran.choice(base))
       i+=1
   return(li)
print(seq_alea(15))
