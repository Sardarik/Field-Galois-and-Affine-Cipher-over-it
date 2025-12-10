import math

from galois_functions import *
from affine_functions import *

print("Hi! Please choose if you want to work with:\n 1 - Galois Field\n 2 - Affine Cipher over Galois Field")
first_choice = int(input())
            
            
if first_choice == 1:
    print("Please choose if you want to:\n 1. Construct a Galois Field\n 2. Generate all irreducible polynomials for a Galois Field\n "
          "3. Perform addition or multiplication with presented polynomials\n 4. Find generator elements of the multiplicative group of the Galois Field and decompose elements of this group into powers of the chosen generator")
    galois_second_choice = int(input())
    if galois_second_choice == 1:
        print("Please choose if you want to construct a Galois Field by using:\n 1. p and n\n 2. Irreducible polynomial")
        galois_third_choice = int(input())
        if galois_third_choice == 1:
                print("Please enter p:")
                p = int(input())
                print("Now enter n:")
                n = int(input())
                for poly in galois_field(p,n):
                    print(poly)
        if galois_third_choice == 2:
            print("Please enter your irreducible polynomial number by number. When you are done enter '!'")
            ir_poly = []
            while True:
                s = input()
                if s == '!':
                    break
                ir_poly.append(int(s))
            print("")
            for poly in galois_field(irreducible_poly=ir_poly):
                print(poly)
    if galois_second_choice == 2:
        print("Please enter p:")
        p = int(input())
        print("Now enter n:")
        n = int(input())
        polys = galois.irreducible_polys(p, n)  
        for f in polys:
            print(f)
    if galois_second_choice == 3:
        print("Please enter p:")
        p = int(input())
        print("Now enter n:")
        n = int(input())
        GF = galois.GF(p**n)  

        print("Please enter the amount of polynomials you want to work with")
        amount = int(input())
        polys = []
        print("Now put in the polynomials themselves, when you're done with each one type in '!'")
        while amount !=0:
            poly = []
            while True:
                s = input()
                if s == '!':
                    break
                poly.append(int(s))
            polys.append(Poly(poly, field=GF))
            amount-=1

        print("Choose the operation:\n 1. Addition\n 2. Multiplication")
        operation = int(input())
        print(combine_polynomials(p,n, polys, operation))
    if galois_second_choice == 4:
        print("Please enter p:")
        p = int(input())
        print("Now enter n:")
        n = int(input())
        print("Please choose if you want to:\n 1. Find all the generators of the field\n 2. Decompose elements of this group into powers of the chosen generator")
        galois_third_choice = int(input())
        if galois_third_choice == 1:
            gens = find_generators_and_groups(p, n)
            for g in gens: print(g)
        if galois_third_choice == 2:
            print("Please type in the number of the generator:")
            x = int(input())
            groups = find_generators_and_groups(p,n, x)
            g0, elems_powers = groups[0]  
            for elem, k in elems_powers[:15]: 
                print(f"{g0}^{k} = {elem}")           


    
if first_choice == 2:
    print("Let's try to encrypt and decrypt texts together using affine cipher over Galois field")
    print("You can only use english in your text, so be careful!")
    print('Please input your key now, but follow these rules:\n   1. The key is supposed to look like that: Number Space Number (i.e. 7 3)\n   2. The first number can not be 0')
    print('Now input the key:')
    a_key = input()
    a_key = [int(x) for x in a_key.split()]
    a = int(a_key[0])
    b = int(a_key[1])
    print("Now input n:")
    n = int(input())
    while True:
        if a!=0:
            print("Choose if you want to:\n   1.Encrypt\n   2.Decrypt\nWrite down only a number")
            second_affine_choice = int(input())
            if second_affine_choice == 1:
                print("Input the text you want to encrypt here:")
                ae_text = input()
                print(f'Your answer is: {affine_cipher_encrypt(ae_text, a_key, n)[1]}')
                break
            if second_affine_choice == 2:
                print("Input the text you want to decrypt here:")
                ad_text = input()
                _, encrypted_elements = b64_into_field(ad_text, n)
                print(f'Your answer is: {affine_cipher_decrypt(encrypted_elements, a_key, n)}')
                break
            else:
                continue
        else:
            print('Please choose another key')
            a_key = input()
            a_key = [int(x) for x in a_key.split()]
            a = int(a_key[0])
            b = int(a_key[1])
    
    
