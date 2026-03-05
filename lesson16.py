  
a={
    'A':[1, 2, 2, 3, 4, 4],
    'B':[2, 3, 7, 9, 10, 2],
    'C':[10, 11, 12, 14, 14]
}
b={}
for i, j in a.items():
    b.update({i:sum(set(j))})
print(b)
    
    #! FUNKSIYA - DEF

  