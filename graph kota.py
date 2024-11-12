class Peta:
    def __init__(self):
        self.daftar_kota = {}
    
    def print_peta(self):
        for kota in self.daftar_kota:
            print(kota, ":",self.daftar_kota[kota])
        
    def tambah_kota(self,kota):
        if kota not in self.daftar_kota:
            self.daftar_kota[kota] = []
            return True
        return False
    
    def hapus_kota(self,kotaDihapus):
        #cek apakah kota yang ingin dihapus ada di list
        if kotaDihapus in self.daftar_kota:
        #iterasi setiap kotalain untuk hapus kotadihapus
            for kotalain in self.daftar_kota:
                #cek apakah kota yang ingin dihapus ada jalannya ke kotalain
                if kotaDihapus in self.daftar_kota[kotalain]:
                    self.daftar_kota[kotalain].remove(kotaDihapus)
            del self.daftar_kota[kotaDihapus]
            return True
        return False
    
    def tambah_jalan(self,kota1,kota2):
        if kota1 in self.daftar_kota and kota2 in self.daftar_kota:
            #masukkan kota 1 di list kota2
            self.daftar_kota[kota2].append(kota1)
            #masukkan kota 2 di list kota1
            self.daftar_kota[kota1].append(kota2)
            return True
        return False
    
    def hapus_jalan(self,kota1,kota2):
        if kota1 in self.daftar_kota and kota2 in self.daftar_kota:
            #hapus kota 1 di list kota2
            self.daftar_kota[kota2].remove(kota1)
            #hapus kota 2 di list kota1
            self.daftar_kota[kota1].remove(kota2)
            return True
        return False
        

peta_jawatengah = Peta()
peta_jawatengah.tambah_kota("Semarang")
peta_jawatengah.tambah_kota("Demak")
peta_jawatengah.tambah_kota("Kudus")
peta_jawatengah.tambah_kota("Pati")
peta_jawatengah.tambah_kota("Salatiga")
peta_jawatengah.tambah_kota("Boyolali")
peta_jawatengah.tambah_kota("Kendal")
peta_jawatengah.tambah_kota("Temanggung")
peta_jawatengah.tambah_kota("Wonosobo")
peta_jawatengah.tambah_kota("Banjarnegara")

peta_jawatengah.tambah_jalan("Semarang","Demak")
peta_jawatengah.tambah_jalan("Semarang","Salatiga")
peta_jawatengah.tambah_jalan("Semarang","Kendal")
peta_jawatengah.tambah_jalan("Semarang","Temanggung")
peta_jawatengah.tambah_jalan("Demak","Kudus")
peta_jawatengah.tambah_jalan("Kudus","Pati")
peta_jawatengah.tambah_jalan("Salatiga","Boyolali")
peta_jawatengah.tambah_jalan("Temanggung","Wonosobo")
peta_jawatengah.tambah_jalan("Wonosobo","Banjarnegara")

print('-' * 70)
peta_jawatengah.print_peta()