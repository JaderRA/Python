def sort(v):
    for j in v:
        i=0
        while i<len(v)-1:
            if v[i]>=v[i+1]:
                x=v[i]
                v[i]=v[i+1]
                v[i+1]=x
            i+=1
    return v

vetor=input('Digite os números do vetor, separados por um espaço:')
l=list(map(int, vetor.split(' ')))
sort(l)
print(l)