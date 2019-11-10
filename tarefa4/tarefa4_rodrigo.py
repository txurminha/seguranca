def somatorio(inicio, fim, razao):
    
    an = (fim - (fim-1) % razao) - 1            # Encontra o último número múltiplo do intervalo
    a1 = inicio - (inicio % razao) + razao      # Encontra o primeiro número múltiplo do intervalo
    n = ((an - a1) / razao) + 1
    print('an = {}, a1 = {} n = {}'.format(an,a1,n))
    return (n/2) * (a1 + an)

print('{}'.format(somatorio(0,1000000,3) + somatorio(0,1000000,5) - somatorio(0,1000000,15)))
 