'''
Created on 19/07/2013

@author: M@RVIN
'''

f=open("ola k ase.txt","r")
i=0
lines=[]
for line in f:
    linea=line.split(',')
    lines.append(linea)
    i=i+1
    print ("\n")
i=0
j=0
while i<9:
    j=0
    while j<9:
        print (lines[i][j])
        j=j+1
    i=i+1