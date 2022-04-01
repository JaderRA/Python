def remove_repetidos(v):
    v.sort()
    for i in v:
        j=0
        while j<len(v)-1:
            if v[j]==v[j+1]:
                v.pop(j)
            j+=1
    return v   
n=[1,2,2,3,1,4,4,4,8,7,7,8,9,9]
print(remove_repetidos(n))

