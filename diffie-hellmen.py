from Crypto.Random import random, get_random_bytes
from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


iv = get_random_bytes(AES.block_size)

def power(a, b, p): 
    return pow(a, b, p)

def generate_private_key(a): 
    return random.getrandbits(a)

def generate_public_key(private_key, q, a): 
    return pow(a, private_key) % q

def compute_shared_secret(their_public_key, private_key, q):
    return pow(their_public_key, private_key) % q

def send_message(message, iv, sender_key,  reciever_key):
    """Simulates sending a message between users with """
    message = pad(message, AES.block_size)
    cipher = AES.new(sender_key, AES.MODE_CBC, iv=iv)
    encryption = cipher.encrypt(message)
    cipher = AES.new(reciever_key, AES.MODE_CBC, iv= iv)
    return unpad(cipher.decrypt(encryption), AES.block_size)

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

    sha_alice = sha256(bytes(k_alice)).digest()[:16]
    sha_bob = sha256(bytes(k_bob)).digest()[:16]
    
    m0 = b'Hi Alice!'
    print(send_message(m0, iv, sha_bob, sha_alice))
    m1 = b'Hi Bob!'
    print(send_message(m1, iv, sha_alice, sha_bob))

    


if __name__ == "__main__": 
    main()