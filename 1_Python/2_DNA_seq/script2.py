#verilen dizi 5 tane tandem repeat şekline getirilir.

def tandem_repeat(dizi, tekrar_sayisi=5):
    return dizi * tekrar_sayisi

dna_dizisi = 'AGCTATAG'
tandem_dna_dizisi = tandem_repeat(dna_dizisi)