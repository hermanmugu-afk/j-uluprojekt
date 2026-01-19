while True:
    """Kasutaja sisestab oma nime, praeguse parooli ja soovitud uue parooli"""
    nimi = input("sisesta nimi: ")
    vanaparool = input("Sisesta oma praegune parool: ")
    uusparool = input("Sisesta oma uus parool: ")

    """kontrollin kas paroolid on samad"""
    if vanaparool == uusparool:
        print("Uus ja vana parool ei tohi olla samasugused. Proovi uuesti.")
        continue

    """kontrollin kas vanaparoolis on uusparool"""
    if vanaparool in uusparool:
        print("Uues paroolis ei tohi olla vana parooli. Proovi uuesti.")
        continue

    """Kontrollin, kas uues paroolis on vana parool tagurpidi"""
    if vanaparool[::-1] in uusparool:
        print("Parool ei tohi olla sama mis vana parool tagurpidi. Proovi uuesti.")
        continue

    """Kontrollin, kas uus parool on täpselt sama mis kasutaja nimi"""
    if nimi == uusparool:
        print("Parool ei tohi olla sama mis nimi. Proovi uuesti.")
        continue

    """Kontrollin, kas uus parool sisaldab kasutaja nime"""
    if nimi in uusparool:
        print("Parool ei tohi sisaldada kasutajanime. Proovi uuesti.")
        continue

    """Kontrollin, kas uus parool sisaldab kasutaja nime tagurpidi"""
    if nimi[::-1] in uusparool:
        print("Parool ei tohi sisaldada nime tagurpidi. Proovi uuesti.")
        continue

    """kontrollin kas parool on Õige pikkusega(8-64)"""

    if len(uusparool) < 8 or len(uusparool) > 64:
        print("Parool on vale pikkusega. Proovi uuesti.")
        continue

    """kontrollin kas sisaldab vähemalt ühte suurt tähte"""

    sisaldabsuur = False
    for symbol in uusparool:
            if symbol.isupper():
                sisaldabsuur = True

    if sisaldabsuur == False:
        print("Parool peab sisaldama vähemalt ühte suurt tähte. Proovi uuesti.")
        continue

    """kontrollin kas sisaldab vähemalt ühte väikest tähte"""

    sisaldabväike = False

    for symbol in uusparool:
            if symbol.islower():
                sisaldabväike = True
    if sisaldabväike == False:
        print("Parool peab sisaldama vähemalt ühte väikest tähte")
        continue  

    """kontrollin et parool ei sisaldaks tühikut"""
    isspace = False
    for symbol in uusparool:
        if symbol.isspace():
                isspace = True
    if isspace == True:
         print("Ei tohi tühikuid olla. Proovi uuesti.")
         continue
            
    """kontrollin et parool sisaldaks vähemalt ühte sümbolit"""
    alnum = False    
    for symbol in uusparool:
        if not symbol.isalnum():
                alnum = True
    if alnum == False:
        print("Parool ei sisalda sümbolit. Proovi uuesti.")
        continue
    
    """Parool on korrektne ja läbis testid"""
    print("Parool edukalt vahetatud!")
    break
