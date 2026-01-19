"""Kasutaja sisestab oma nime, praeguse parooli ja soovitud uue parooli"""
nimi = input("sisesta nimi: ")
vanaparool = input("Sisesta oma praegune parool: ")
uusparool = input("Sisesta oma uus parool: ")

"""kontrollin kas paroolid on samad"""
if vanaparool == uusparool:
    print("paroolid on samad")
"""kontrollin kas vanaparoolis on uusparool"""
if vanaparool in uusparool:
     print("vanaparoolis on uusparool")
"""Kontrollin, kas uues paroolis on vana parool tagurpidi"""
if vanaparool[::-1] in uusparool:
     print("parool ei tohi olla vana parool tagurpidi")
"""Kontrollin, kas uus parool on täpselt sama mis kasutaja nimi"""
if nimi == uusparool:
    print("Parool ei tohi olla sama mis nimi")
"""Kontrollin, kas uus parool sisaldab kasutaja nime"""
if nimi in uusparool:
    print("Parool ei tohi sisaldada nime")
"""Kontrollin, kas uus parool sisaldab kasutaja nime tagurpidi"""
if nimi[::-1] in uusparool:
    print("Parool ei tohi sisaldada nime tagurpidi")


"""kontrollin kas parool on 6ige pikkusega(8-64)"""

if len(uusparool) < 8 or len(uusparool) > 64:
     print("parool on vale pikkusega")

 
"""kontrollin kas sisaldab v2hemalt yhte suurt t2hte"""

sisaldabsuur = False

for symbol in uusparool:
        if symbol.isupper():
            sisaldabsuur = True

if sisaldabsuur == False:
    print("parool peab sisaldama v2hemalt yhte suurt t2hte")  

"""kontrollin kas sisaldab v2hemalt yhte väikest t2hte"""

sisaldabväike = False

for symbol in uusparool:
        if symbol.islower():
            sisaldabväike = True
if sisaldabväike == False:
    print("parool peab sisaldama vähemalt yhte väikest tähte")  

for symbol in uusparool:
     if symbol.isspace():
        print("Ei tohi olla tyhikut")
        break
     
alnum = False    
for symbol in uusparool:
     if not symbol.isalnum():
            alnum = True
if alnum == False:
    print("parool ")
