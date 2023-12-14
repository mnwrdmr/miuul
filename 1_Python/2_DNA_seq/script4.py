#verilen dizinin RNA dizisine çevrilmesi
def rnaya_cevir(dizi):
    return dizi.replace('T', 'U')

dna_dizisi = 'AGCTATAG'
rna_dizisi = rnaya_cevir(dna_dizisi)