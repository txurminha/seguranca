def calcula_inv_mul(mod):
    #mod = int(input('Módulo: '))
    for i in range(mod):
        for j in range(mod):
            if ((i*j)%mod) == 1:
                print('Inverso de {} mod {} = {}'.format(i, mod, j))

    print()

calcula_inv_mul(21)
calcula_inv_mul(94)



