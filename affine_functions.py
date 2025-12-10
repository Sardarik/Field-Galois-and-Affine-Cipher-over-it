import galois
import base64

def b64_into_field(b64_text, n):
    GF = galois.GF(2**n)
    raw_bytes = base64.b64decode(b64_text)
    bits = ''.join(format(byte, '08b') for byte in raw_bytes)
    return GF, [GF(int(bits[i:i+n].ljust(n, '0'), 2)) for i in range(0, len(bits), n)]

def field_to_b64(elements, n):
    binary_blocks = [format(int(element), f'0{n}b') for element in elements]
    all_bits = ''.join(binary_blocks)
    encrypted_bytes = bytes(int(all_bits[i:i+8], 2) for i in range(0, len(all_bits), 8))
    return base64.b64encode(encrypted_bytes).decode('ascii')


def affine_cipher_encrypt(text, key, n):
    text_b64 = base64.b64encode(text.encode('ascii')).decode('ascii')
    GF, elements = b64_into_field(text_b64, n)
    
    a = GF(int(key[0]))
    b = GF(int(key[1]))
    encrypted_elements = [a * element + b for element in elements]
    encrypted_b64 = field_to_b64(encrypted_elements, n)
    return encrypted_elements, encrypted_b64

def affine_cipher_decrypt(encrypted_elements, key, n):
    GF = galois.GF(2**n)
    a = GF(int(key[0]))
    b = GF(int(key[1]))
    a_inv = GF(1) / a
    decrypted_elements = [a_inv * (C - b) for C in encrypted_elements]

    decrypted_b64 = field_to_b64(decrypted_elements, n)
    decrypted_text =base64.b64decode(decrypted_b64).decode('ascii').rstrip('\x00')
    return decrypted_text

