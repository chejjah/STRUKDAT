class Node:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, nama, harga):
        new_node = Node(nama, harga)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.nama, current.harga)
            current = current.next

    def total_harga(self):
        total = 0
        current = self.head
        while current is not None:
            total += current.harga
            current = current.next
        return total

# Menu Miexue
menu = LinkedList()
menu.add("Miexue Ice Cream", 5000)
menu.add("Boba Shake", 16000)
menu.add("Mi Sundae", 14000)
menu.add("Mi Ganas", 11000)
menu.add("Creamy Mango Boba", 22000)

# Pesanan
keranjang = LinkedList()

# Tambah pesanan ke keranjang
def tambah_pesanan(nama, harga):
    keranjang.add(nama, harga)

# Tampilkan pesanan yang sudah ditambahkan
def tampil_pesanan():
    keranjang.display()

# Jumlah Harga yang dibayarkan
def jumlah_harga():
    return keranjang.total_harga()

# Penggunaan
tambah_pesanan("Miexue Ice Cream", 5000)
tambah_pesanan("Boba Shake", 16000)
tambah_pesanan("Mi Sundae", 14000)
tambah_pesanan("Mi Ganas", 11000)
tambah_pesanan("Creamy Mango Boba", 22000)

tampil_pesanan()
print("Jumlah Harga yang dibayarkan:", jumlah_harga())