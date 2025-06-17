list_buku = []
while True:
    print("Daftar Buku")
    judul = str(input("Masukkan judul buku: "))
    penulis = str(input("Masukkan penulis buku: "))

    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)

    print("No.|  Judul  | Penulis")
    for index, buku in enumerate(list_buku):
        print(f"{index + 1}. |  {buku[0]} | {buku[1]}")

    lanjut = str(input("Lanjut gak? (y/n): "))
    if lanjut == "n":
        break
print("Makasih udah daftarin buku!")