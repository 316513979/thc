def contar_v1(adn, base):
    adn=list(adn)
    i = 0
    for c in adn:
        if c == base:
            i += 1
    return i

def contar_v2(adn, base):
    i = 0
    for c in adn:
        if c == base:
            i += 1
    return i

adn='ATGCGACCTAT'
base='C'
print contar_v1(adn, base)
print contar_v2(adn, base)
print n
print '%s aparece %d veces en %s' % (base, n, adn)
