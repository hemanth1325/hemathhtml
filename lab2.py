


import csv
with open('lab1.csv') as f :
    reader=csv.reader(f)
    data=list(reader)

sp=data[1][:-1]
gn=[['?' for _ in range(len(sp))]for _ in range(len(sp))]

for i in data:
    if i[-1]=='Yes':
        for j in range(len(sp)):
            if i[j]!=sp[j]:
                sp[j]='?'
                gn[j][j]='?'
    elif i[-1]=='No':
        for j in range(len(sp)):
            if i[j]!=sp[j]:
                
                gn[j][j]=sp[j]
    else:
        gn[j][j]='?'
    print(gn)
    print(sp)
