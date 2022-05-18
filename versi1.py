
listOrder = {}
listOrdername = {}
listAddons = {}
listAddonsName = {}
listCost = {}

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
    print("-"*69)
    print("|    [D]        |        Tanpa Fasilitas       |   Rp. 0            |")

    print("="*69)

def order():

    # header
    print("\n")
    print("="*107)
    print("| INPUT PEMBAYARAN TRAVEL             |")

    # Input nama
    print("="*107)
    name = str(input("| Nama Peserta                        | : "))

    # Input kode paket
    print("-"*107)
    package = str(input("| Kode paket                          | : "))
    listOrder[name] = package
    print("-"*107)
    
    # menampilkan nama paket
    def namaPaket():
        if (package == "01"):
            print("| Nama paket                          | : Karawang - Pantai Pakis ")
            listOrdername[name] = 'Karawang - Pantai Pakis'
        elif (package == "02"):
            print("| Nama paket                          | : Karawang - Curug Cigentis - Gunung Sanggabuana ")
            listOrdername[name] = 'Karawang - Curug Cigentis - Gunung Sanggabuana'
        elif (package == "03"):
            print("| Nama paket                          | : Karawang - Candi Jiwa ")
            listOrdername[name] = 'Karawang - Candi Jiwa'
        elif (package == "04"):
            print("| Nama paket                          | : Karawang - Pantai Samudra ")
            listOrdername[name] = 'Karawang - Pantai Samudra'
        else :
            print("| Nama paket                          | : Cek kembali kode paket yang anda masukan ")
            listOrdername[name] = "-"
    namaPaket()

    # menampilkan Tarif paket   
    def tarifPaket():
        print("-"*107)
        if (package == "01"):
            print("| Tarif paket                         | : Rp. 1.000.000 ")
    
        elif (package == "02"):
            print("| Tarif paket                         | : Rp. 500.000 ")
    
        elif (package == "03"):
            print("| Tarif paket                         | : Rp. 600.000 ")

        elif (package == "04"):
            print("| Tarif paket                         | : Rp. 850.000 ")

        else :
            print("| Tarif paket                         | : Cek kembali kode paket yang anda masukan ")
    tarifPaket()
    
    # input kode tambahan
    print("-"*107)
    addons = str(input("| Kode tambahan                       | : "))
    listAddons[name] = addons 

    # Menampilkan fasilitas 
    
    def Addons():
        print("-"*107)
        if (addons == "A"):
            print("| Fasilitas                           | : Penginapan ")
            listAddonsName[name] = "Penginapan"
        elif (addons == "B"):
            print("| Fasilitas                           | : Penjemputan ")
            listAddonsName[name] = "Penjemputan"
        elif (addons == "C"):
            print("| Fasilitas                           | : Kuliner ")
            listAddonsName[name] = "Kuliner"
        elif (addons == "D"):
            print("| Fasilitas                           | : - ")
            listAddonsName[name] = "-"
        else:
            print("| Fasilitas                           | : Cek kembali kode paket yang anda masukan ")
            listAddonsName[name] = "-"
    Addons()

    # Menampilkan tarif fasilitas 
    
    def tarifAddons():
        print("-"*107)
        if (addons == "A"):
            print("| Tarif tambahan                      | : Rp. 600.000 ")
    
        elif (addons == "B"):
            print("| Tarif tambahan                      | : Rp. 300.000 ")
    
        elif (addons == "C"):
            print("| Tarif tambahan                      | : Rp. 300.000 ")

        elif (addons == "D"):
            print("| Tarif tambahan                      | : Rp. 0 ")

        else:
            print("| Fasilitas                           | : Cek kembali kode paket yang anda masukan ")
    tarifAddons()


    # Hitung jumlah tarif
    print("-"*107)
    
    # hitung harga paket
    if (package == "01"):
        packageCost = 1000000
    elif (package == "02"):
        packageCost = 500000
    elif (package == "03"):
        packageCost = 600000
    elif (package == "04"):
        packageCost = 850000
    else:
        packageCost = 0
    
    # Hitung harga Fasilitas tambahan

    if (addons == "A"):
        addCost = 600000
    elif (addons == "B"):
        addCost = 300000
    elif (addons == "C"):
        addCost = 300000
    else:
        addCost = 0

    print("| Jumlah tarif                        | : Rp. ",packageCost+addCost)


    # menampilkan ppn 11 %
    print("-"*107)
    print("| PPN 11%                             | : Rp. ",int((packageCost+addCost)*11/100))

    # menampilkan jumlah biaya
    print("-"*107)
    print("| Jumlah biaya                        | : Rp. ",int(packageCost+addCost+(packageCost+addCost)*11/100))
    print("="*107)

    listCost[name] = int(packageCost+addCost+(packageCost+addCost)*11/100)

def ShowData():
    keyListOrder = list(listOrder.keys()) # Mengubah dictionary jadi list

    print("\n")
    print("="*135)
    print("| NO. | Nama Peserta          | Nama Paket                                            | Fasilitas tambahan    | Jumlah tarif          |")
    print("="*135)

    for x in range(len(keyListOrder)):
        # No
        print("|",x+1,end='')
        print(" "*(4-len(str(x+2))),end='')

        # Nama peserta
        print("|",keyListOrder[x],end='')
        print(" "*(22-len(keyListOrder[x])),end='')

        # Nama paket
        print("|",listOrdername[keyListOrder[x]],end='')
        print(" "*(54-len(listOrdername[keyListOrder[x]])),end='')

        # Penginapan
        print("|",listAddonsName[keyListOrder[x]],end='')
        print(" "*(22-len(listAddonsName[keyListOrder[x]])),end='')

        # Jumlah tarif
        print("| Rp.",listCost[keyListOrder[x]],end='')
        print(" "*(17-len(str(listCost[keyListOrder[x]]))),'|')

        print("="*135)

def searchData():
    try:
        keyListOrder = list(listOrder.keys()) # Mengubah dictionary jadi list

        inputan = str(input("Nama Pelanggan : "))
        x = keyListOrder.index(inputan)

        print("\n")
        print("="*135)
        print("| NO. | Nama Peserta          | Nama Paket                                            | Fasilitas tambahan    | Jumlah tarif          |")
        print("="*135)


        # No
        print("|",x+1,end='')
        print(" "*(4-len(str(x+2))),end='')
        # Nama peserta
        print("|",keyListOrder[x],end='')
        print(" "*(22-len(keyListOrder[x])),end='')
        # Nama paket
        print("|",listOrdername[keyListOrder[x]],end='')
        print(" "*(54-len(listOrdername[keyListOrder[x]])),end='')
        # Penginapan
        print("|",listAddonsName[keyListOrder[x]],end='')
        print(" "*(22-len(listAddonsName[keyListOrder[x]])),end='')
        # Jumlah tarif
        print("| Rp.",listCost[keyListOrder[x]],end='')
        print(" "*(17-len(str(listCost[keyListOrder[x]]))),'|')
        print("="*135)
    except ValueError:
        print("Data yang di cari tidak ada ")

    

# Fungsi untuk delete data

def deleteData():
    try:
        deleteName = str(input("Nama pelanggan : "))

        del listOrder[deleteName]
        del listOrdername[deleteName]
        del listAddons[deleteName]
        del listAddonsName[deleteName]
        del listCost[deleteName]
        print("Data pelanggan sudah berhasil di hapus :)")
    except:
        print("\Data tidak ditemukan")

# Fungsi untuk edit data

def editData():
    try:
        print("Silakan isi data yang akan di edit")
        deleteName = str(input("Nama pelanggan : "))

        del listOrder[deleteName]
        del listOrdername[deleteName]
        del listAddons[deleteName]
        del listAddonsName[deleteName]
        del listCost[deleteName]

        print("Silakan isi Data yang baru")
        order()
    except:
        print("\nData tidak ditemukan")




#fungsi untuk menampilkan menu
def show_menu():
    print ("\n")
    print ("===================== MENU ===================")
    print ("| [1] Show Daftar paket & Fasilitas tambahan |")
    print ("| [2] Show Data                              |")
    print ("| [3] Insert Data                            |")
    print ("| [4] Edit Data                              |")
    print ("| [5] Delete Data                            |")
    print ("| [6] Exit                                   |")
    print ("| [7] Search Data                            |")
    print ("==============================================")
    
    menu = input("\nPILIH MENU> ")
    
    if menu == "1":
        menuPaket()
        menuAddons()
    elif menu == "2":
        ShowData()
    elif menu == "3":
        order()
    elif menu == "4":
        editData()
    elif menu == "5":
        deleteData()
    elif menu == "6":
        exit()
    elif menu == "7":
        searchData()
    else:
        print("Salah pilih!")
        
if __name__ == "__main__":
    
    while(True):
        show_menu()




