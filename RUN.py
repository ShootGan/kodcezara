alfabet = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"
cz = []
odszyfrowane = ""
szyfr = input("wprowadz szyfr: ")
szyfr = szyfr.lower()

for leter in alfabet:
    cz.append(szyfr.count(leter))
klucz = cz.index(max(cz))
for x in szyfr:
    if x in alfabet:
        odszyfrowane = odszyfrowane + alfabet[alfabet.index(x) - klucz]
    else:
        odszyfrowane = (odszyfrowane + x)

print(odszyfrowane)
