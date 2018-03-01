import random

def bord2v2():
    #Leikurinn gengur út á að leikmadur kastar ut og annad hvort veidir fisk(1) eda ekki(0). Einskonar happdraetti. Leikmadur vinnur thegar hann hefur veitt thrja fiska i rod.
    kast0 = 0
    kast1 = 0
    kast2 = 0
    #Summa telur hvort leikmadur velji rett thrisvar i rod, þ.e. hvort thad se fiskur eda ekki.
    summa = kast0 + kast1 + kast2
    #While lykkjan telur hvort summan verdi ad 3 en tha hoppar madur ut fyrir og vinnur!
    #Sidasta kastinu er hent ut og bara skodud 3 gildi i einu en annad er otharfi.
    #Leikmadur faer stig tho hann kasti ekki ef thad aetti ekki a fiskast.
    while (summa<=3):
        kastaut = input("Viltu kasta út núna? Veldu 1 fyrir já og 0 fyrir nei.")
        kast = random.randint(0,1)
        kast2 = kast1
        kast1 = kast0

        if (kastaut == kast):
            kast0 = 1
        else:
            kast0 = 0

    print("Til hamingju þú vannst borðið!!!")
    return summa
