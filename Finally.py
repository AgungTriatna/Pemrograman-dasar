import os

# Variabel umum

listNamaPeserta = []
listKodePaket = []
listNamaPaket = []
listTarifpaket = []
listKodeTambahan = []
listFasilitas = []
listTarifTambahan = []
listJumlahTarif = []
listPPN =[]
listJumlahBiaya = []
temporary = {}
simbol = "!@#$%^&*|\\{[}]':;<>~`.,?"

def menuPaket():
    print("""\n                      
                                P A K E T   W I S A T A   K A R A W A N G                              
===========================================================================================================
| Kode Paket |                  Rute perjalanan               |    Minimum Peserta   |       Tarif        |
-----------------------------------------------------------------------------------------------------------
|    [01]    |              Karawang - Pantai Pakis           |        6 Orang       |   Rp. 1.000.000    |
-----------------------------------------------------------------------------------------------------------
|    [02]    | Karawang - Curug Cigentis - Gunung Sanggabuana |        6 Orang       |   Rp. 500.000      |
-----------------------------------------------------------------------------------------------------------
|    [03]    |              Karawang - Candi Jiwa             |        4 Orang       |   Rp. 600.000      |
-----------------------------------------------------------------------------------------------------------
|    [04]    |            Karawang - Pantai Samudra           |        5 Orang       |   Rp. 850.000      |
===========================================================================================================""")

def menuAddons():
    print("""\n                 
                    L A Y A N A N  T A M B A H A N         
=====================================================================
| Kode Tambahan |        Fasilitas             |       Tarif        |
=====================================================================
|    [A]        |        Penginapan            |   Rp. 600.000      |
---------------------------------------------------------------------
|    [B]        |        Penjemputan           |   Rp. 300.000      |
---------------------------------------------------------------------
|    [C]        |        Kuliner               |   Rp. 300.000      |
=====================================================================\n""")

def header():
    print("\n")
    menuPaket()
    print("\n")
    print("="*107)
    print("| INPUT PEMBAYARAN TRAVEL                                                                                 |")
    print("="*107)

def inputnama():

    nama = str(input("| Nama Peserta                        | : "))

    if(len(nama) == 0):
            print("-"*107)
            print("| Nama Peserta                        | : Nama tidak boleh kosong dan berisi simbol, isi kembali nama pertama")
            print("-"*107)
            inputnama()
    elif(nama == " " or nama == "  "):
            print("-"*107)
            print("| Nama Peserta                        | : Nama tidak boleh kosong dan berisi simbol, isi kembali nama pertama")
            print("-"*107)
            inputnama()
    elif(len(nama) != 0):        
        for x in range(len(nama)):
        
            if(nama[x] in simbol):
                print("-"*107)
                print("| Nama Peserta                        | : Nama tidak boleh kosong dan berisi simbol, isi kembali nama kedua")
                print("-"*107)
                x += 1
                inputnama()
                break
            else:
                temporary['nama'] = nama
            
    
def inputKodePaket():
    print("-"*107)
    paket = str(input("| Kode paket                          | : "))
    print("-"*107)
    temporary['kodepaket'] = paket
    showNamaPaket()

def showNamaPaket():
    paket = temporary['kodepaket']
    if (paket == "01" or paket == "1"):
        print("| Nama paket                          | : Karawang - Pantai Pakis ")
        print("-"*107)
        temporary['namapaket'] = 'Karawang - Pantai Pakis'
        print("| Tarif paket                         | : Rp. 1.000.000 ")
        print("-"*107)
        temporary['tarifpaket'] = int(1000000)
    elif (paket == "02" or paket == '2'):
        print("| Nama paket                          | : Karawang - Curug Cigentis - Gunung Sanggabuana ")
        temporary['namapaket'] = 'Karawang - Curug Cigentis - Gunung Sanggabuana'
        print("-"*107)
        print("| Tarif paket                         | : Rp. 500.000 ")
        print("-"*107)
        temporary["tarifpaket"] = int(500000)
    elif (paket == "03" or paket == '3'):
        print("| Nama paket                          | : Karawang - Candi Jiwa ")
        temporary['namapaket'] = 'Karawang - Candi Jiwa'
        print("-"*107)
        print("| Tarif paket                         | : Rp. 600.000 ")
        print("-"*107)
        temporary["tarifpaket"] = int(600000)
    elif (paket == "04" or paket == '4'):
        print("| Nama paket                          | : Karawang - Pantai Samudra ")
        temporary['namapaket'] = 'Karawang - Pantai Samudra'
        print("-"*107)
        print("| Tarif paket                         | : Rp. 850.000 ")
        print("-"*107)
        temporary["tarifpaket"] = int(850000)
    else :
        print("| Nama paket                          | : Kode yang anda masukan salah, silakan masukan kode lagi ")
        inputKodePaket()


def inputFasilitas():
    question = str(input("\nFasilitas tambahan ? (y/n) : "))
    paket = temporary['kodepaket']

    try:

        if(question=='y' or question=='Y'):

            # Menambahkan fasilitas
            menuAddons()
            print("-"*107)
            kodeTambahan = str(input("| Kode tambahan                       | : "))
            temporary['kodetambahan'] = kodeTambahan
            print("-"*107)

            # Menampilkan Fasilitas

            if (kodeTambahan == "A" or kodeTambahan == "a"):
                print("| Fasilitas                           | : Penginapan ")
                temporary['fasilitas'] = "Penginapan"
                print("-"*107)
            elif (kodeTambahan == "B" or kodeTambahan == "b"):
                print("| Fasilitas                           | : Penjemputan ")
                temporary['fasilitas'] = "Penjemputan"
                print("-"*107)
            elif (kodeTambahan == "C" or kodeTambahan == "c"):
                print("| Fasilitas                           | : Kuliner ")
                temporary['fasilitas'] = "Kuliner"
                print("-"*107)
            else:
                print("\n Kode yang di inputkan salah")
                inputFasilitas()

            # Menampilkan tarif fasilitas
            
            hitungtariffasilitas()

            # Hitung jumlah tarif
            
            hitungjumlahtarif()
            

            # menampilkan ppn 11 %
            
            hitungppn()

            # menampilkan jumlah biaya
            hitungjumlahbiaya()

            # os.system('cls')

            showDetail()

        elif(question=='n' or question == 'N'):

            # Menambahkan fasilitas kosong

            print("-"*107)
            print(("| Kode tambahan                       | : - "))
            temporary['kodetambahan'] = '-'
            print("-"*107)

            # Tampilkan fasilitas kosong
            print("| Fasilitas                           | : -")
            temporary['fasilitas'] = '-'

            # Menampilkan tarif tambahan
            print("-"*107)
            print("| Tarif tambahan                      | : -")
            temporary['tariftambahan'] = '-'

            # Menampilkan tarif fasilitas
            
            hitungtariffasilitas()

            # Hitung jumlah tarif
            
            hitungjumlahtarif()
            

            # menampilkan ppn 11 %
            
            hitungppn()

            # menampilkan jumlah biaya
            hitungjumlahbiaya()

            # os.system('cls')

            showDetail()
        
        else:
            print("\nKeyword yang anda masukan salah, silakan masukan lagi ")
            inputFasilitas()
            
    except:
        # Menambahkan fasilitas kosong

            print("-"*107)
            print(("| Kode tambahan                       | : - "))
            listKodeTambahan.append("-")
            print("-"*107)

            # Tampilkan fasilitas kosong
            print("| Fasilitas                           | : -")
            listFasilitas.append("-")

            # Menampilkan tarif tambahan
            print("-"*107)
            print("| Tarif tambahan                      | : -")
            listTarifTambahan.append(0)

            # Menampilkan jumlah tarif 
            print("-"*107)
            print("| Jumlah tarif                        | : Rp.",temporary['jumlahtarif'])
            hitungjumlahtarif()

            # menampilkan ppn 11 %
            print("-"*107)
            print("| PPN 11%                             | : Rp.",temporary['ppn'])
            hitungppn()


            # menampilkan jumlah biaya
            print("-"*107)
            print("| Jumlah biaya                        | : Rp.",temporary['jumlahbiaya'])
            print("="*107)

            


            os.system('cls')

            showDetail()

def hitungtariffasilitas():

    kodeTambahan = temporary['kodetambahan']

    if (kodeTambahan == "A" or kodeTambahan == "a"):
        print("| Tarif tambahan                      | : Rp. 600.000 ")
        temporary['tariftambahan'] = int(600000)

    elif (kodeTambahan == "B" or kodeTambahan == "b"):
        print("| Tarif tambahan                      | : Rp. 300.000 ")
        temporary['tariftambahan'] = int(300000)

    elif (kodeTambahan == "C" or kodeTambahan == "c"):
        print("| Tarif tambahan                      | : Rp. 300.000 ")
        temporary['tariftambahan'] = int(300000)

    else:
        print("| Fasilitas                           | : - ")
        temporary['tariftambahan'] = int(0)

def hitungjumlahtarif():

    jumlahtarif = temporary['tarifpaket'] + temporary['tariftambahan']
    temporary['jumlahtarif'] = jumlahtarif

def hitungppn():
    ppn = int(11/100*temporary['jumlahtarif'])
    temporary['ppn'] = ppn


def hitungjumlahbiaya():

    print("-"*107)
    totalbiaya = int(temporary['tarifpaket'] + temporary['tariftambahan'] + temporary["ppn"])
    # print("| Jumlah biaya                        | : Rp.",totalbiaya)
    # print("="*107)

    temporary['jumlahbiaya'] = totalbiaya

def savedata():
    
    listNamaPeserta.append(temporary['nama'])
    listKodePaket.append(temporary['kodepaket'])
    listNamaPaket.append(temporary['namapaket'])
    listTarifpaket.append(temporary['tarifpaket'])
    listKodeTambahan.append(temporary['kodetambahan'])
    listFasilitas.append(temporary['fasilitas'])
    listTarifTambahan.append(temporary['tariftambahan'])
    listJumlahTarif.append(temporary['jumlahtarif'])
    listPPN.append(temporary['ppn'])
    listJumlahBiaya.append(temporary['jumlahbiaya'])

    
   
def showDetail():
    print("\n")
    print("="*107)
    print("D E T A I L  P E M B A Y A R A N".center(107))
    print("="*107)
    print("| Nama Peserta                        | :",temporary['nama'])
    print("="*107)
    print("| Kode paket                          | :",temporary['kodepaket'])
    print("="*107)
    print("| Nama Paket                          | :",temporary['namapaket'])
    print("="*107)
    print("| Tarif Paket                         | : Rp.",temporary['tarifpaket'])
    print("="*107)
    print("| Kode Tambahan                       | :",temporary['kodetambahan'])
    print("="*107)
    print("| Fasilitas                           | :",temporary['fasilitas'])
    print("="*107)
    print("| Tarif Tambahan                      | : Rp.",temporary['tariftambahan'])
    print("="*107)
    print("| Jumlah Tarif                        | : Rp.",temporary['jumlahtarif'])
    print("="*107)
    print("| PPN 11%                             | : Rp.",temporary['ppn'])
    print("="*107)
    print("| Jumlah Biaya                        | : Rp.",temporary['jumlahbiaya'])
    print("="*107)

    
def questionSaveData():
    
    question = str(input("\nSIMPAN DATA ? (Y/N) : "))
    if(question=='Y' or question=='y'):
        savedata()
        print("Data berhasil disimpan")
    elif(question=='N' or question=='n'):
        show_menu()
    else:
        print("\nData yang di masukan salah, silahkan masukkan kembali")
        questionSaveData()
        
def questionEditData():
    
    question = str(input("\nSIMPAN DATA ? (Y/N) : "))
    if(question=='Y' or question=='y'):
        editNo = temporary['editNo']
        
        listNamaPeserta[editNo] = temporary['nama']
        listKodePaket[editNo] = temporary['kodepaket']
        listNamaPaket[editNo] = temporary['namapaket']
        listTarifpaket[editNo] = temporary['tarifpaket']
        listKodeTambahan[editNo] = temporary['kodetambahan']
        listFasilitas[editNo] = temporary['fasilitas']
        listTarifTambahan[editNo] = temporary['tariftambahan']
        listJumlahTarif[editNo] = temporary['jumlahtarif']
        listPPN[editNo] = temporary['ppn']
        listJumlahBiaya[editNo] = temporary['jumlahbiaya']
        print("Data berhasil diedit")
    elif(question=='N' or question=='n'):
        show_menu()
    else:
        print("\nData yang di masukan salah, silakan masukkan kembali")
        questionEditData()

def ShowData():

    print("\n")
    print("="*135)
    print("| NO. | Nama Peserta          | Nama Paket                                            | Fasilitas tambahan    | Jumlah tarif          |")
    print("="*135)

    if(len(listNamaPeserta)==0):
        print("|                                             T I D A K    A D A     D A T A                                                          |")
        print("="*135)
    else:
        for x in range(len(listNamaPeserta)):
            # No
            print("|",x+1,end='')
            print(" "*(4-len(str(x+2))),end='')

            # Nama peserta
            print("|",listNamaPeserta[x],end='')
            print(" "*(22-len(listNamaPeserta[x])),end='')

            # Nama paket
            print("|",listNamaPaket[x],end='')
            print(" "*(54-len(listNamaPaket[x])),end='')

            # Fasilitas
            print("|",listFasilitas[x],end='')
            print(" "*(22-len(listFasilitas[x])),end='')

            # Jumlah tarif
            print("| Rp.",int(listJumlahBiaya[x]),end='')
            print(" "*(17-len(str(listJumlahBiaya[x]))),'|')

            print("="*135)


def searchData():
    try:

        inputan = str(input("Nama Pelanggan : "))

        print("\n")
        print("="*135)
        print("| NO. | Nama Peserta          | Nama Paket                                            | Fasilitas tambahan    | Jumlah tarif          |")
        print("="*135)

        if(len(listNamaPeserta)!=0):

            for x in range(len(listNamaPeserta)):
                if(listNamaPeserta[x]==inputan):

                    # No
                    print("|",x+1,end='')
                    print(" "*(4-len(str(x+2))),end='')

                    # Nama peserta
                    print("|",listNamaPeserta[x],end='')
                    print(" "*(22-len(listNamaPeserta[x])),end='')

                    # Nama paket
                    print("|",listNamaPaket[x],end='')
                    print(" "*(54-len(listNamaPaket[x])),end='')

                    # Penginapan
                    print("|",listFasilitas[x],end='')
                    print(" "*(22-len(listFasilitas[x])),end='')

                    # Jumlah tarif
                    print("| Rp.",int(listJumlahBiaya[x]),end='')
                    print(" "*(17-len(str(listJumlahBiaya[x]))),'|')
                    print("="*135)
        if(len(listNamaPeserta)==0):
            print("|                                             T I D A K    A D A     D A T A                                                          |")
            print("="*135)            
        # else:
        #     print("|                                             T I D A K    A D A     D A T A                                                          |")
        #     print("="*135)
    except:
        print("|                                             T I D A K    A D A     D A T A                                                          |")
        print("="*135)    

def order():

    header()
    inputnama()
    inputKodePaket()
    inputFasilitas()
    questionSaveData()


# Fungsi untuk delete data

def deleteData():
    try:
        if (len(listNamaPeserta)!= 0):
            ShowData()
            deleteNo = int(input("Pilih No. urut yang akan di hapus : "))-1

            listNamaPeserta.remove(listNamaPeserta[deleteNo])
            listKodePaket.remove(listKodePaket[deleteNo])
            listNamaPaket.remove(listNamaPaket[deleteNo])
            listTarifpaket.remove(listTarifpaket[deleteNo])
            listKodeTambahan.remove(listKodeTambahan[deleteNo])
            listFasilitas.remove(listFasilitas[deleteNo])
            listTarifTambahan.remove(listTarifTambahan[deleteNo])
            listPPN.remove(listPPN[deleteNo])
            listJumlahBiaya.remove(listJumlahBiaya[deleteNo])
            print("Data pelanggan sudah berhasil di hapus :)")
        else:
            ShowData()
    except:
        print("Data tidak ditemukan")

# Fungsi untuk edit data

def editData():
    try:
        if(len(listNamaPeserta) != 0 ):
            ShowData()
            print("\nPilih data yang ingin di edit")
            editNo = int(input("No : "))-1
            if editNo < len(listNamaPeserta):
                temporary['editNo'] = editNo
                header()
                inputnama()
                inputKodePaket()
                inputFasilitas()
                questionEditData()
            else:
                print ("Data Tidak Di Temukan")
        else:
            ShowData()

    except:
        print("\nData tidak ditemukan")


def show_menu():
    print ("\n")
    print ("===================== MENU ===================")
    print ("| [1] Show Daftar paket & Fasilitas tambahan |")
    print ("| [2] Insert Data                            |")
    print ("| [3] Show Data                              |")
    print ("| [4] Edit Data                              |")
    print ("| [5] Delete Data                            |")
    print ("| [6] Search Data                            |")
    print ("| [7] Exit                                   |")
    print ("==============================================")
    
    menu = input("\nPILIH MENU> ")
    
    if menu == "1":
        menuPaket()
        menuAddons()
    elif menu == "2":
        order()
    elif menu == "3":
        ShowData()
    elif menu == "4":
        editData()
    elif menu == "5":
        deleteData()
    elif menu == "6":
        searchData()
    elif menu == "7":
        exit()
    else:
        print("Salah pilih!")
        
if __name__ == "__main__":
    
    while(True):
        show_menu()

