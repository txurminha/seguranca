def tot(n) :
    result = n # Initialize result as n

    # Consider all prime factors
    # of n and for every prime
    # factor p, multiply result with (1 – 1/p)
    p=2
    while(p*p<=n) :

        # Check if p is a prime factor.
        if (n % p == 0) :
            # If yes, then update n and result
            while (n % p == 0) :
                n = n // p
                result = result * (1.0 - (1.0 / (float) (p)))
        p = p + 1

    # If n has a prime factor
    # greater than sqrt(n)
    # (There can be at-most one such prime factor)
    if (n > 1) :
        result = result * (1.0 - (1.0 / (float)(n)))

    return (int)(result)


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m



def test():
    # n = 1073
    # e = 71
    # c = 436
    
    in_list = input().split(' ')
    # print(in_list)
    n = int(in_list[0])
    e = int(in_list[1])
    c = int(in_list[2])

    phi = tot(n)
    #print(tot(n), e)

    d = modinv(e, phi)

    return pow(c, d)%n
    # return(d)


print(test())