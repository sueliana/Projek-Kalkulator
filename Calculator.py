def menu():
    kalkulator=("kalkulator bermenu","1. tambah","2. tolak","3. darab","4. bahagi","5. kuasa","6. punca kuasa""7. tamat")
    for i in range(len(kalkulator)):
        print (kalkulator[i])

def no_pilihan_pengguna():
    no_pilihan = 0
    while (no_pilihan < 1)or (no_pilihan > 7):
        no_pilihan = int(input(" pilihan anda [pilih 1 hingga 7]: "))
    return no_pilihan

def dua_no_dr_pengguna():
    no1=int(input("masukkan nombor pertama : "))
    no2=int(input("masukkan nombor kedua : "))
    return no1,no2

def kiracetak(jenisoperator,no1,no2):
    kalkulator2=[no1+no2,no1-no2,no1*no2,no1/no2,no1**no2,(round(no1**(1/no2),2))]
    print(kalkulator2[jenisoperator-1])
    
aktif=1
while aktif==1:
    menu()
    jenisoperasi = no_pilihan_pengguna()
    if jenisoperasi==7:
       aktif =0
    else:
        (no1, no2)=dua_no_dr_pengguna()
        kiracetak(jenisoperasi,no1,no2)
print(" terima kasih kerana menggunakan saya")
