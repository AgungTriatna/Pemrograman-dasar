
listOrder = {}
listOrdername = {}
listAddons = {}
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
menuPaket()


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
menuAddons()


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
            print("| Nama paket                         | : Cek kembali kode paket yang anda masukan ")
    tarifPaket()
    
    # input kode tambahan
    print("-"*107)
    addons = str(input("| Kode paket                          | : "))
    listAddons[name] = addons 

    # Menampilkan fasilitas 
    
    def Addons():
        print("-"*107)
        if (addons == "A"):
            print("| Fasilitas                           | : Penginapan ")
    
        elif (addons == "B"):
            print("| Fasilitas                           | : Penjemputan ")
    
        elif (addons == "C"):
            print("| Fasilitas                           | : Kuliner ")

        else:
            print("| Fasilitas                           | : Cek kembali kode paket yang anda masukan ")
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
    elif (package == "01"):
        packageCost = 850000
    else:
        packageCost = 0
    
    # Hitung harga Fasilitas tambahan

    if (addons == "A"):
        addCost = 600000
    elif (addons == "B"):
        addCost = 300000
    elif (addons == "c"):
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

order()
print(listOrder)
print(listAddons)
print(listCost)

def listpeserta():
    keyListOrder = list(listOrder.keys())
    itemlistOrdername = list(listOrdername.items())
    print("="*107)
    print("| NO. | Nama Peserta          | Nama Paket                        |    Fasilitas tambahan   |      Jumlah tarif     |")

    for x in range(len(keyListOrder)):
        print("|",x+1,end='')
        print(" "*(4-len(str(x+2))),end='')
        print("|",keyListOrder[x],end='')
        print(" "*(22-len(keyListOrder[x])),end='')
        print("|",listOrdername[keyListOrder[x]])

         

listpeserta()

