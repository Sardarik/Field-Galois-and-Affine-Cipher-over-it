import galois
from galois import Poly
from itertools import product

def galois_field(p=None,n=None, irreducible_poly=None):
    if irreducible_poly is not None:
        unique_coeffs = set(irreducible_poly)
        p = max(unique_coeffs) + 1    
        n = len(irreducible_poly) - 1
    GF=galois.GF(p)
    elements = GF.elements
    for i in product(elements, repeat=n):
        poly = Poly(i,field=GF)
        yield poly


def combine_polynomials(p, n, polys, operation):
    GF=galois.GF(p**n)
    field = polys[0].field                            
    irreducible_poly = GF.irreducible_poly
    coeffs = irreducible_poly.coeffs  
    irr_over_GF = Poly(coeffs, field=GF)

    if operation == 1:
        result = Poly.Zero(field=field)
        for f in polys:
            result += f
        return result

    elif operation == 2:
        result = Poly.One(field=GF)
        for f in polys:
            result *= f
        result = result % irr_over_GF
        return result


def prime_factors(x):
    factors = []
    d = 2
    while d * d <= x:
        if x % d == 0:
            factors.append(d)
            while x % d == 0:
                x //= d
        d += 1
    if x > 1:
        factors.append(x)
    return factors



def find_generators_and_groups(p, n, x=None):
    GF = galois.GF(p**n)
    m = p**n-1 
    factors = prime_factors(m)
    generators = []
    result = []

    for a in GF.elements[1:]: 
        is_generator = True
        
        for r in factors:
            power = m // r
            if a ** power == GF(1):
                is_generator = False
                break
        
        if is_generator:
            b = [x for x in bin(a)[2:]]
            poly = Poly(b, field=GF)
            generators.append(a)
            result.append(poly)

    groups = []
    
    if x is not None:
        GF = galois.GF(p**n)
        g = generators[x]
        elems_powers = []
        current = GF(1)
         
        
        for k in range(m):
            elems_powers.append((poly, k))
            current *= g
            b = [x for x in bin(current)[2:]]
            poly = Poly(b, field=GF)
        groups.append((int(g), elems_powers))
        return groups
    
    return result

