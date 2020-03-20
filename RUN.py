alfabet="aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"
cz = []
odszyfrowane = ""
szyfr =input("wprowadz szyfr: ")

for leter in alfabet:
    cz.append(szyfr.count(leter))
klucz = cz.index(max(cz))
for x in szyfr:
    if x == chr(32):
        odszyfrowane = odszyfrowane + (chr(32))
    else:
        odszyfrowane = odszyfrowane + alfabet[alfabet.index(x) - klucz]

print(odszyfrowane)

