def tagihan_listrik(jmlh_pemakaian,golongan=3):
    pemaiaikan_awal = 100
    pemakaian_selanjutnya = jmlh_pemakaian - pemaiaikan_awal
    if golongan == 1:
        bayar = pemaiaikan_awal * 1500 + pemakaian_selanjutnya * 2000
    elif golongan == 2:
        bayar = pemaiaikan_awal * 2500 + pemakaian_selanjutnya * 3000
    elif golongan == 3:
        bayar = pemaiaikan_awal * 4000 + pemakaian_selanjutnya * 5000
    elif golongan == 4:
        bayar = pemaiaikan_awal * 5000 + pemakaian_selanjutnya * 7000
    return bayar

print(tagihan_listrik(130))
print(tagihan_listrik(80,4))
print(tagihan_listrik(golongan=1,jmlh_pemakaian=175))




