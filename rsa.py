from Crypto.Util.number import getPrime

def mod_power(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 ==1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base*base) % modulus

    return result


def mod_inverse(a,m):
    def egcd(a,b):
        if a ==0: return (b,0,1)
        else:
            g, y, x = egcd(b%a, a)
            return (g, x -(b//a) * y, y)
        
    g, x, _ = egcd(a, m)
    if g != 1: raise Exception('Modular inverse does not exist')
    else: return x % m

def int_ascii(num):
    return bytes.fromhex(hex(num)[2:])
        

if __name__ == '__main__':
    print('Task 1')
    # Get your prime numbers
    p = getPrime(2048)
    q = getPrime(2048)
    while q == p:
        q = getPrime(2048)
    
    # Setup necessary variables
    n = p * q
    phi = (p-1) * (q-1)
    e = 65537
    d = mod_inverse(e, phi)

    # Public and private keys
    PU = (e, n)
    PR = (d,n)

    # Encrypt desired message using Bob's public key
    M = 'Hello Bob!'
    print('Alice is sending message:', M)
    int_M = int(M.encode().hex(), 16)
    C = mod_power(int_M, e, n)

    # Bob decrypts Alice's message with his private key
    D = mod_power(C, d, n)
    M2 = int_ascii(D)
    print('Bob recieved message:', M2)
    print('\n\n\n\n')
    
    print('Task 2')

    # Alice encrypts her message
    M = 'How are you doing Bob?'
    print('Alice is sending message:', M)
    int_M = int(M.encode().hex(), 16)
    C = mod_power(int_M, e, n)

    # Mallory recieves the cipher and changes it to C_prime
    r = 2
    C_prime = (C * mod_power(r, e, n)) % n

    # Mallory sends C_prime to Bob
    D = mod_power(C_prime, d, n)
    M2 = int_ascii(D)
    print('Bob recieved message:', M2)

    # Result recieved is
    print('Mallory could decrypt:', int_ascii(D//2))