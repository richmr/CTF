def vignere_decode(ciphertext, key):
    plaintext = ""
    posn = 0
    ciphertext = ciphertext.upper()
    key = key.upper()
    base = ord('A')
    for letter in ciphertext:
        Ci = ord(letter) - base
        Ki = ord(key[posn % len(key)]) - base
        Mi = (Ci - Ki) + base
        plaintext += chr(Mi)
        posn += 1
    print "decoded: {}".format(plaintext)
    return plaintext

vignere_decode("MVT-7K5L:COO", "MCA-5A597C9B")


def vignere_encode(plaintext, key):
    ciphertext = ""
    posn = 0
    plaintext = plaintext.upper()
    key = key.upper()
    base = ord('A')
    for letter in plaintext:
        Mi = ord(letter)-base
        Ki = ord(key[posn % len(key)]) - base
        Ci = (Mi + Ki) + base
        ciphertext += chr(Ci)
        posn += 1
    print "enciphered: {}".format(ciphertext)
    return ciphertext

vignere_encode("attackatdawn", "MCA-5a597c9b")


def vignere_getKey2(plaintext, ciphertext):
    # plaintext and ciphertext shoiuld be same length.
    # using an absolute reference from 'A' this time
    # capitalizing the inputs
    base = ord('A')
    plaintext = plaintext.upper()
    ciphertext = ciphertext.upper()
    key = ""
    for posn in range(len(plaintext)):
        Mi = ord(plaintext[posn])-base
        Ci = ord(ciphertext[posn])-base
        Ki = (Ci - Mi) + base
        key += chr(Ki)
    print "the key: {}".format(key)
    return key

vignere_getKey2("attackatdawn", "mvt-7k5l:coo")

       

