class Node:
    def __init__(self, menu, harga):
         self.menu = menu
         self.harga = harga
         self.next = None

class Keranjang:
     def __init__(self, menu, harga):
        self.head = None
        self.lenght = 0

     def tambah_pesanan(self, menu, harga):
        menu_baru = Node(menu, harga)
        temp = self.head
        if temp == None:
            self.head = menu_baru
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = menu_baru
        self.lenght += 1

     def tampilkan_pesanan(self):
        temp = self.head
        while temp is not None:
            print(f"{temp.menu} {temp.harga} rupiah")
            temp = temp.next
        print("Jumlah Total Pesanan Anda Adalah: ", self.lenght)

     def total_harga(self):
        total = 0
        temp = self.head
        while temp:
            total += temp.harga
            temp = temp.next
        print(f"Total pesanan anda yang harus dibayar: {total} rupiah")

def main():
    menu_miexue = {
        "miexue ice cream": 5000,
        "boba shake": 16000,
        "mi sundae": 14000,
        "mi ganas": 11000,
        "creamy mango boba": 22000
    }

    keranjang_pesanan = Keranjang("y",0)

    while True:
        print("\nMenu:")
        print("1. Pesan menu")
        print("2. Tampilkan pesanan")
        print("3. Bayar pesanan")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            print("""
Selamat Datang di Miexue
Pilihan Menu Makanan
Miexue Ice Cream   = Rp.5.000
Boba Shake         = Rp.16.000
Mi Sundae          = Rp.14.000
Mi Ganas           = Rp.11.000
Creamy Mango Boba  = Rp.22.000""")
            pesanan = input("Masukkan menu yang ingin dipesan: ").lower()
            if pesanan in menu_miexue:
                keranjang_pesanan.tambah_pesanan(pesanan, menu_miexue[pesanan])
                print(f"{pesanan} sudah ditambahkan ke keranjang")
            else:
                print("Menu tidak tersedia")
        elif pilihan == "2":
            print("Pesanan:")
            keranjang_pesanan.tampilkan_pesanan()
        elif pilihan == "3":
            keranjang_pesanan.total_harga()
            break
        elif pilihan == "4":
            print("Terima kasih, sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi")

main()