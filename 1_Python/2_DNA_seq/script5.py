#verilen dizinin kodonlar halinde gruplandırılması
# örnek : AGCTATAGT
# AGC TAT AGT

#fonksiyonun tanımlanması:

def kodonlara_ayir(dizi):
    kodonlar = []
    for i in range(0, len(dizi), 3):
        kodonlar.append(dizi[i:i+3])
    return kodonlar

#ana program:

dna_dizisi = 'AGCTATAGT'
kodonlar = kodonlara_ayir(dna_dizisi)

#######################
#baska nasil yapabiliriz ?

def kodonlara_ayir(dna_dizisi):
    return [dna_dizisi[i:i+3] for i in range(0, len(dna_dizisi), 3)]

# Ana program
dna_dizisi = "AGCTATAGT"
kodonlar = kodonlara_ayir(dna_dizisi)
print("Kodonlar:", kodonlar)

#######################

#######################
# Mesela list comprehension ile nasil yazilabilir?

def kodonlara_ayir(dna_dizisi):
    return [dna_dizisi[i:i+3] for i in range(0, len(dna_dizisi)-2, 3)]

# Ana program
dna_dizisi = "AGCTATAGT"
kodonlar = kodonlara_ayir(dna_dizisi)
print("Kodonlar:", kodonlar)
########################

#######################
# range fonksiyonunun 3. parametresi nedir?

#Bu kodda range fonksiyonunun üçüncü parametresi 3'tür. Şu bölümde görülebilir:

#range(0, len(dna_dizisi)-2, 3)
#Bu ifade, 0 ile len(dna_dizisi)-2 arasındaki sayıları 3'er 3'er atlayarak üretecektir.
# Yani, 0, 3, 6, 9, ... gibi değerleri içeren bir aralık üretecektir.
# Bu, dna_dizisi üzerinde her seferinde üçlü gruplara denk gelen indisleri ifade eder.
#######################

#######################
# append fonksiyonu nedir?

#append listelere eleman eklemek için kullanılır.

# dizi[i:i+3] ifadesi ne yapar?
#bu ifade dilimleme slicinng için kullanılır yani i den başla
#i+3 elemnanına kadar bir index oluştur. bu dna dizisini 3erli gruplara böl.
#######################
