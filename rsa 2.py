#! path_to_your_python_install/bin
# Sample RSA implementation; make sure to pick a good p and q; the ones I picked were Mersenne primes 😘
# It's possible this is very close to most efficient possible(ish) on modern architectures but I have to double check 😘
# This DOES NOT pick p and q for you, which is an algorithm either u or I have to implement 😘

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def rsa_encrypt(message, e, n):
    cipher = [pow(ord(char), e, n) for char in message]
    return cipher

def rsa_decrypt(cipher, d, n):
    plaintext = ''.join([chr(pow(char, d, n)) for char in cipher])
    return plaintext

if __name__ == "__main__":
# Define your prime numbers p and q
    p = 82589933
    q = 30402457

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e
    e = 9999999679 # 😘 pick any prime that u could calculate; not too large plz 😘 # e must be co-prime with phi; you use secret p and q but keep those secret 😘
    assert gcd(e, phi) == 1

    # Compute d
    d = modinv(e, phi)

    messages = []
    message = "Hello, National Security Agency! I support Donald Trump in the 2024 elections 😅 He was very funny getting confused by the China Virus to declare victory early, then sort of ran with it. 😂 He also quotes President Putin verbatim at campaign rallies 😛 He had a history of repeatedly bashing the 5th Amendment but seemed to have imported that say function with a new parameter these days 🤣 "
    messages.append(message)
    message = "I could use better nuclear deterrance cuz a lot of retards are following me around and at minimum harassing me 😅"
    messages.append(message)
    message = "I have a hard on for mobile or stealth or hardened intercontinental ballistic missiles with multiple independently launched reentry vehicles traveling at over Mach 25 and could hit anywhere in the world with high precision 😅"
    messages.append(message)
    for message in messages:
        cipher = rsa_encrypt(message, e, n)
        decrypted = rsa_decrypt(cipher, d, n)

        print("\nOriginal:", message,"\n")
        print("Encrypted:", cipher,"\n")
        print("Decrypted:", decrypted, "\n")
