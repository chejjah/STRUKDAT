
from itertools import permutations

class WeightedGraph:
    # Initialization
    def __init__(self):
        self.cityList = {}

    def printGraph(self):
        # Mengiterasi setiap city
        for kota in self.cityList:
            # Setiap kota print nama kota
            print(kota, ":", self.cityList[kota])

            # Print distances to neighboring cities
            for tetangga, distance in self.cityList[kota].items():
                # Print tetangga dan jarak
                print("    ->", tetangga, ":", distance)

    def tambah_kota(self, kota):
        # Jika kota tidak ada di cityList
        if kota not in self.cityList:
            # Maka tambahkan kota
            self.cityList[kota] = {}
            return True
        return False

    def hapusKota(self, kotaDihapus):
        # Jika kotaDihapus ada di cityList
        if kotaDihapus in self.cityList:
            # Remove the city from the city list
            del self.cityList[kotaDihapus]
            # Remove references to the deleted city from other cities
            for kota in self.cityList:
                # Jika kotaDihapus ada di cityList[kota]
                if kotaDihapus in self.cityList[kota]:
                    # Maka hapus kotaDihapus
                    del self.cityList[kota][kotaDihapus]
            return True
        return False

    def tambah_jalan(self, kota1, kota2, jarak):
        if kota1 in self.cityList and kota2 in self.cityList:
            self.cityList[kota1][kota2] = jarak
            self.cityList[kota2][kota1] = jarak
            return True
        return False

    def hapusJalan(self, kota1, kota2):
        if kota1 in self.cityList and kota2 in self.cityList:
            if kota2 in self.cityList[kota1]:
                del self.cityList[kota1][kota2]
                del self.cityList[kota2][kota1]
                return True
        return False

    def dijkstra(self, source):
        # Initialize distances with infinity
        # distances = {city: float('inf') for city in self.cityList}
        
        distances = {}
        for kota in self.cityList:
            distances[kota] = float('inf')
        
        distances[source] = 0
        print (distances)
        # Initialize list of unvisited cities
        unvisited_cities = []
        for kota in self.cityList:
            unvisited_cities.append(kota)
        # unvisited_cities = list(self.cityList.keys())
        print (unvisited_cities)

        while unvisited_cities:
            # Find the unvisited city with the smallest distance
            jarak_minimal = float('inf')
            kota_terdekat = None
            # Mengiterasi setiap kota yang belum dikunjungi
            for kota in unvisited_cities:
                # Jika jarak kota lebih kecil dari min_distance
                if distances[kota] < jarak_minimal:
                    jarak_minimal = distances[kota]
                    kota_terdekat = kota

            # Remove the closest city from unvisited list
            unvisited_cities.remove(kota_terdekat)

            # Update distances to neighboring cities
            for tetangga, weight in self.cityList[kota_terdekat].items():
                # Jika jarak kota terdekat + weight lebih kecil dari jarak kota tetangga
                distance = distances[kota_terdekat] + weight
                if distance < distances[tetangga]:
                    distances[tetangga] = distance

        return distances
    
    def tsp(self):
        # Initialize variables
        jarak_terpendek = float('inf')
        jalur_terpendek = []

        # Generate all permutations of cities
        cities = list(self.cityList.keys())
        for path in permutations(cities):
            # Calculate total distance for current permutation
            total_distance = 0
            for i in range(len(path) - 1):
                if path[i] in self.cityList and path[i + 1] in self.cityList[path[i]]:
                    total_distance += self.cityList[path[i]][path[i + 1]]
                else:
                    total_distance = float('inf')
                    break  # Break if path is invalid
            # Check if current permutation is shorter than the current shortest path
            if total_distance < jarak_terpendek:
                jarak_terpendek = total_distance
                jalur_terpendek = path

        return jalur_terpendek, jarak_terpendek

# Example usage with Dijkstra's algorithm:
peta_jawatengah = WeightedGraph()
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

peta_jawatengah.tambah_jalan("Semarang","Demak", 33)
peta_jawatengah.tambah_jalan("Semarang","Salatiga", 51)
peta_jawatengah.tambah_jalan("Semarang","Kendal", 31)
peta_jawatengah.tambah_jalan("Semarang","Temanggung", 80)
peta_jawatengah.tambah_jalan("Demak","Kudus", 26)
peta_jawatengah.tambah_jalan("Kudus","Pati", 24)
peta_jawatengah.tambah_jalan("Salatiga","Boyolali", 24)
peta_jawatengah.tambah_jalan("Temanggung","Wonosobo", 39)
peta_jawatengah.tambah_jalan("Wonosobo","Banjarnegara", 47)

peta_jawatengah.printGraph()
shortest_distances = peta_jawatengah.dijkstra("Semarang")
print("Shortest distances from Semarang to other cities:")
for kota, jarak in shortest_distances.items():
    print(kota, ":", jarak)
jalur_terpendek, jarak_terpendek = peta_jawatengah.tsp()
print("Jalur TSP terpendek:", jalur_terpendek)
print("Jarak TSP terpendek:", jarak_terpendek)