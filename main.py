
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


def menuPaket():
    print("\n                                  P A K E T   W I S A T A   K A R A W A N G  "                            )
    print("="*107)
    print("| Kode Paket |                  Rute perjalanan               |    Minimum Peserta   |       Tarif        |")
    print("="*107)
    print("|    [01]    |              Karawang - Pantai Pakis           |        6 Orang       |   Rp. 1.000.000    |")
    print("-"*107)
    print("|    [02]    | Karawang - Curug Cigentis - Gunung Sanggabuana |        6 Orang       |   Rp. 500.000      |")
    print("-"*107)
    print("|    [03]    |              Karawang - Candi Jiwa             |        4 Orang       |   Rp. 600.000      |")
    print("-"*107)
    print("|    [04]    |            Karawang - Pantai Samudra           |        5 Orang       |   Rp. 850.000      |")
    print("="*107)

def menuAddons():
    print("\n                 L A Y A N A N  T A M B A H A N         "           )
    print("="*69)
    print("| Kode Tambahan |        Fasilitas             |       Tarif        |")
    print("="*69)
    print("|    [A]        |        Penginapan            |   Rp. 600.000      |")
    print("-"*69)
    print("|    [B]        |        Penjemputan           |   Rp. 300.000      |")
    print("-"*69)
    print("|    [C]        |        Kuliner               |   Rp. 300.000      |")
    print("="*69)
    print("\n")

def order():

    # header
    print("\n")
    menuPaket()
    print("\n")
    print("="*107)
    print("| INPUT PEMBAYARAN TRAVEL                                                                                 |")

    # Input nama
    print("="*107)
    nama = str(input("| Nama Peserta                        | : "))
    listNamaPeserta.append(nama)

    # Input kode paket
    print("-"*107)
    paket = str(input("| Kode paket                          | : "))
    listKodePaket.append(paket)

    print("-"*107)
    
    # menampilkan nama paket
    def namaPaket():
        if (paket == "01"):
            print("| Nama paket                          | : Karawang - Pantai Pakis ")
            listNamaPaket.append('Karawang - Pantai Pakis')
        elif (paket == "02"):
            print("| Nama paket                          | : Karawang - Curug Cigentis - Gunung Sanggabuana ")
            listNamaPaket.append('Karawang - Curug Cigentis - Gunung Sanggabuana')
        elif (paket == "03"):
            print("| Nama paket                          | : Karawang - Candi Jiwa ")
            listNamaPaket.append('Karawang - Candi Jiwa')
        elif (paket == "04"):
            print("| Nama paket                          | : Karawang - Pantai Samudra ")
            listNamaPaket.append('Karawang - Pantai Samudra')
        else :
            print("| Nama paket                          | : Cek kembali kode paket yang anda masukan ")
            listNamaPaket.append("-")
    namaPaket()

    # menampilkan Tarif paket   
    def tarifPaket():
        print("-"*107)
        if (paket == "01"):
            print("| Tarif paket                         | : Rp. 1.000.000 ")
            print("-"*107)
            listTarifpaket.append(1000000)
            temporary["cost"] = int(1000000)
        elif (paket == "02"):
            print("| Tarif paket                         | : Rp. 500.000 ")
            print("-"*107)
            listTarifpaket.append(500000)
            temporary["cost"] = int(500000)
        elif (paket == "03"):
            print("| Tarif paket                         | : Rp. 600.000 ")
            print("-"*107)
            listTarifpaket.append(600000)
            temporary["cost"] = int(600000)
        elif (paket == "04"):
            print("| Tarif paket                         | : Rp. 850.000 ")
            print("-"*107)
            listTarifpaket.append(850000)
            temporary["cost"] = int(850000)
        else :
            print("| Tarif paket                         | : Cek kembali kode paket yang anda masukan ")
            print("-"*107)
            listTarifpaket.append(0)
            temporary["cost"] = int(0)
    tarifPaket()

    # input kode tambahan

    question = str(input("\nFasilitas tambahan ? (y/n) : "))

    if(question=='y' or question=='Y'):

        # Menambahkan fasilitas
        menuAddons()
        print("-"*107)
        kodeTambahan = str(input("| Kode tambahan                       | : "))
        listKodeTambahan.append(kodeTambahan)
        print("-"*107)

        # Menampilkan Fasilitas

        if (kodeTambahan == "A" or kodeTambahan=="a"):
            print("| Fasilitas                           | : Penginapan ")
            listFasilitas.append("Penginapan")
            print("-"*107)
        elif (kodeTambahan == "B" or kodeTambahan=="b"):
            print("| Fasilitas                           | : Penjemputan ")
            listFasilitas.append("Penjemputan")
            print("-"*107)
        elif (kodeTambahan == "C" or kodeTambahan=="c"):
            print("| Fasilitas                           | : Kuliner ")
            listFasilitas.append("Kuliner")
            print("-"*107)
        else:
            print("| Kode tambahan                       | : -")
            print("-"*107)
            listFasilitas.append("-")

        # Menampilkan tarif fasilitas

        if (kodeTambahan == "A" or kodeTambahan == "a"):
            print("| Tarif tambahan                      | : Rp. 600.000 ")
            listTarifTambahan.append(60000)
    
        elif (kodeTambahan == "B" or kodeTambahan == "b"):
            print("| Tarif tambahan                      | : Rp. 300.000 ")
            listTarifTambahan.append(300000)
    
        elif (kodeTambahan == "C" or kodeTambahan == "c"):
            print("| Tarif tambahan                      | : Rp. 300.000 ")
            listTarifTambahan.append(300000)

        else:
            print("| Fasilitas                           | : - ")
            listTarifTambahan.append(0)


    
        # Hitung jumlah tarif

        print("-"*107)

        if (paket == "01"):
            hargaPaket = 1000000
        elif (paket == "02"):
            hargaPaket = 500000
        elif (paket == "03"):
            hargaPaket = 600000
        elif (paket == "04"):
            hargaPaket = 850000
        else:
            hargaPaket = 0

        # Hitung harga Fasilitas tambahan

        if (kodeTambahan == "A" or kodeTambahan == 'a'):
            hargaTambahan = 600000
        elif (kodeTambahan == "B" or kodeTambahan == 'b'):
            hargaTambahan = 300000
        elif (kodeTambahan == "C" or kodeTambahan == 'c'):
            hargaTambahan = 300000
        else:
            hargaTambahan = 0

        print("| Jumlah tarif                        | : Rp.",hargaPaket+hargaTambahan)
        listJumlahTarif.append(int(hargaPaket+hargaTambahan))


        # menampilkan ppn 11 %
        print("-"*107)
        print("| PPN 11%                             | : Rp.",int((hargaPaket+hargaTambahan)*11/100))
        listPPN.append(int(hargaPaket+hargaTambahan)*11/100)

        # menampilkan jumlah biaya
        print("-"*107)
        print("| Jumlah biaya                        | : Rp.",int(hargaPaket+hargaTambahan+(hargaPaket+hargaTambahan)*11/100))
        print("="*107)

        listJumlahBiaya.append(int(hargaPaket+hargaTambahan+(hargaPaket+hargaTambahan)*11/100))


        
    
    elif(question=='n' or question == 'N'):

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
        print("| Jumlah tarif                        | : Rp.",temporary['cost'])
        listJumlahTarif.append(int(temporary['cost']))

        # menampilkan ppn 11 %
        print("-"*107)
        print("| PPN 11%                             | : Rp.",int(temporary["cost"]*11/100))
        listPPN.append(int(temporary["cost"]*11/100))


        # menampilkan jumlah biaya
        print("-"*107)
        print("| Jumlah biaya                        | : Rp.",int(temporary["cost"]+(temporary["cost"]*11/100)))
        print("="*107)

        listJumlahBiaya.append(int(temporary["cost"]+(temporary["cost"]*11/100)))


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
        else:
            print("|                                             T I D A K    A D A     D A T A                                                          |")
            print("="*135)
    except:
        print("|                                             T I D A K    A D A     D A T A                                                          |")
        print("="*135)

    

# Fungsi untuk delete data

def deleteData():
    try:
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
    except:
        print("Data tidak ditemukan")

# Fungsi untuk edit data

def editData():
    try:
        ShowData()
        print("\nPilih data yang ingin di edit")
        deleteNo = int(input("No : "))-1

        listNamaPeserta.remove(listNamaPeserta[deleteNo])
        listKodePaket.remove(listKodePaket[deleteNo])
        listNamaPaket.remove(listNamaPaket[deleteNo])
        listTarifpaket.remove(listTarifpaket[deleteNo])
        listKodeTambahan.remove(listKodeTambahan[deleteNo])
        listFasilitas.remove(listFasilitas[deleteNo])
        listTarifTambahan.remove(listTarifTambahan[deleteNo])
        listPPN.remove(listPPN[deleteNo])
        listJumlahBiaya.remove(listJumlahBiaya[deleteNo])

        print("Silakan isi Data yang baru")
        order()
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
