#ex page 28

names= {
    "Marie":1, 
    "Bernard":4, 
    "François":2, 
    "Thomas":12, 
    "Hila":15,
    }

# somme=0
# somme= sum(names.values())
# print(somme)

# for i in names.values():
#     somme= somme+i

# moyenne= somme/len(names)
# print(moyenne)  
   

#ex page 31

copy= {}
copy.update(names)

for i, rank in copy.items():
    if rank <=10:
        names.pop(i)

moyenne = sum(names.values()) / len(names)

print(moyenne)

#pas compris






