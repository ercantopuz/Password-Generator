import random
from string import punctuation,ascii_lowercase,ascii_uppercase


def sifreolustur(liste,uzunluk):
    p = ''
    for i in range(0, uzunluk):
        c = random.randint(0, len(liste) - 1)
        gecici = liste[c]
        p += str(random.choice(gecici))
    print('Sifreniz olusturuldu: {} '.format(p))


while True:
    try:
        x=int(input("Sifreniz kac karakter olsun {Cikmak icin 0' a basin}") )
        if (x > 0):
            hepsi = []
            ozelkarolsunMu = raw_input('Ozel karakter olsun mu E ya da H')
            if (ozelkarolsunMu == 'E'):
                hepsi.append(list(punctuation))
            sayiolsunmu = raw_input('Sifrede sayi olsun mu E ya da H')
            if (sayiolsunmu == 'E'):
                hepsi.append(range(0, 10))
            kucukharfolsunMu = raw_input('Kucuk harf olsun mu E ya da H')
            if (kucukharfolsunMu == 'E'):
                hepsi.append(list(ascii_lowercase))
            buyukharfolsunMu = raw_input('Buyuk harf olsun mu E ya da H')
            if (buyukharfolsunMu == 'E'):
                hepsi.append(list(ascii_uppercase))
            if hepsi:
                sifreolustur(hepsi,x)
                break
            else:
                print('Gecersiz cevaplar')
                break
        else:
            print("Cikis yapildi")
            break
    except Exception:
        print('Sayi girmelisiniz')