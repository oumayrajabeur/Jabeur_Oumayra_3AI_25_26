def ricercaDicotomica(l, n):
    i = 0
    f = len(l)-1
    while i <= f:  
        m = (i+f)//2
        print(i, m, f)
        if l[m] == n:
            return True
        elif l[m] > n:
            f=m - 1
        else:
            i = m + 1
    return False
 
 
lista = [10, 12, 44, 72, 88, 96, 104, 1000]
print(ricercaDicotomica(lista, 1000))
