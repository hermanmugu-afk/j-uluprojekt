"""kasutaja sisestab oma praeguse parooli ja soovitud uue parooli"""

vanaparool = input("Sisesta oma praegune parool: ")
uusparool = input("Sisesta oma uus parool: ")

"""kontrollin kas parool on 6ige pikkusega(8-64)"""

if len(uusparool) < 8 or len(uusparool) > 64:
     print("parool on vale pikkusega")