from Crypto.Random import random

def power(a, b, p): 
    return pow(a, b, p)

def generate_private_key(a): 
    return random.getrandbits(a)

def generate_public_key(private_key, q, a): 
    return pow(a, private_key) % q

def compute_shared_secret(their_public_key, private_key, q):
    return pow(their_public_key, private_key) % q

def main(): 
    alpha = 5
    q = 37
    print(f"value of q: {q}")
    print(f"value of alpha: {alpha}")

    #alice keys
    XA = 6
    YA = power(alpha, XA, q)
    print(f"alice private key: {XA}")
    print(f"alice public key: {YA}")

    #bob keys
    XB = 15
    YB = power(alpha, XB, q)
    print(f"bob public key: {XB}")
    print(f"bob private key: {YB}")

    #shared key
    k_alice = power(YB, XA, q)
    k_bob = power(YA, XB, q)
    print(f"alice shared key: {k_alice}")
    print(f"bob shared key: {k_bob}")



if __name__ == "__main__": 
    main()