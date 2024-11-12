from itertools import permutations

class Petajateng:
    def __init__(self):
        self.cityList = {}
    
    def printPeta(self):
        for kota in self.cityList:
            print(kota, ":",self.cityList[kota])
            for neighbor, distance in self.cityList[kota].items():
                print("    ->", neighbor,":",distance)
        
    def tambahkanKota(self,kota):
        #jika kota tidak ada di cityList
        if kota not in self.cityList:
            #maka tambahkan kota
            self.cityList[kota] = {}
            return True
        return False
    
    def hapusKota(self,kotaDihapus):
        #cek apakah kota yang ingin dihapus ada di list
        if kotaDihapus in self.cityList:
            # Remove the city from the city list
            del self.cityList[kotaDihapus]
            # Remove references to the deleted city from other cities
            for kota in self.cityList:
                #jika kotaDihapus ada di cityList[kota]
                if kotaDihapus in self.cityList[kota]:
                    #maka hapus kotaDihapus
                    del self.cityList[kota][kotaDihapus]
            return True
        return False
    
    def tambahkanJalan(self,kota1,kota2,jarak):
        if kota1 in self.cityList and kota2 in self.cityList:
            #masukkan kota 1 di list kota2
            self.cityList[kota2][kota1] = jarak
            #masukkan kota 2 di list kota1
            self.cityList[kota1][kota2] = jarak
            return True
        return False
    
    def hapusJalan(self,kota1,kota2):
        if kota1 in self.cityList and kota2 in self.cityList:
            if kota2 in self.cityList[kota1]:
                del self.cityList[kota1][kota2]
                del self.cityList[kota2][kota1]
                return True
        return False
        
    def dijkstra(self, source):
        # Initialize distances with infinity
        #distances = {city: float('inf') for city in self.cityList}
        
        distances = {}
        for city in self.cityList:
            distances[city] = float('inf')
        
        distances[source] = 0
        print (distances)
        # Initialize list of unvisited cities
        unvisited_cities = []
        for city in self.cityList:
            unvisited_cities.append(city)
        #unvisited_cities = list(self.cityList.keys())
        print (unvisited_cities)

        while unvisited_cities:
            # Find the unvisited city with the smallest distance
            min_distance = float('inf')
            closest_city = None
            #mengiterasi setiap kota yang belum dikunjungi
            for city in unvisited_cities:
                #jika jarak kota lebih kecil dari min_distance
                if distances[city] < min_distance:
                    min_distance = distances[city]
                    closest_city = city

            # Remove the closest city from unvisited list
            unvisited_cities.remove(closest_city)

            # Update distances to neighboring cities
            for neighbor, weight in self.cityList[closest_city].items():
                #jika jarak kota terdekat + weight lebih kecil dari jarak kota tetangga
                distance = distances[closest_city] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance

        return distances
    
    def tsp(self):
        # Initialize variables
        shortest_distance = float('inf')
        shortest_path = []

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
            if total_distance < shortest_distance:
                shortest_distance = total_distance
                shortest_path = path

        return shortest_path, shortest_distance

petaJawaTengah = Petajateng()
#TAMBAH KOTA
petaJawaTengah.tambahkanKota("Kudus")
petaJawaTengah.tambahkanKota("Pati")
petaJawaTengah.tambahkanKota("Demak")
petaJawaTengah.tambahkanKota("Semarang")
petaJawaTengah.tambahkanKota("Rembang")
petaJawaTengah.tambahkanKota("Kendal")
petaJawaTengah.tambahkanKota("Jepara")
petaJawaTengah.tambahkanKota("Salatiga")
petaJawaTengah.tambahkanKota("Surakarta")
petaJawaTengah.tambahkanKota("Grobogan")
petaJawaTengah.tambahkanKota("Blora")
petaJawaTengah.tambahkanKota("Sragen")
petaJawaTengah.tambahkanKota("Temanggung")
petaJawaTengah.tambahkanKota("Boyolali")

#TAMBAH JALAN
petaJawaTengah.tambahkanJalan("Kudus","Demak", 10)
petaJawaTengah.tambahkanJalan("Kudus","Pati", 5)
petaJawaTengah.tambahkanJalan("Kudus","Jepara", 6)
petaJawaTengah.tambahkanJalan("Kudus","Grobogan", 15)
petaJawaTengah.tambahkanJalan("Pati","Rembang", 4)
petaJawaTengah.tambahkanJalan("Pati","Blora", 7)
petaJawaTengah.tambahkanJalan("Pati","Grobogan", 14)
petaJawaTengah.tambahkanJalan("Semarang","Kendal", 11)
petaJawaTengah.tambahkanJalan("Semarang","Salatiga", 8)
petaJawaTengah.tambahkanJalan("Semarang","Demak", 6)
petaJawaTengah.tambahkanJalan("Kendal","Batang", 12)
petaJawaTengah.tambahkanJalan("Kendal","Salatiga", 13)
petaJawaTengah.tambahkanJalan("Kendal","Temanggung", 16)
petaJawaTengah.tambahkanJalan("Surakarta","Salatiga", 9)
petaJawaTengah.tambahkanJalan("Surakarta","Grobogan", 8)
petaJawaTengah.tambahkanJalan("Surakarta","Boyolali", 7)
petaJawaTengah.tambahkanJalan("Surakarta","Sragen", 9)
petaJawaTengah.tambahkanJalan("Rembang","Grobogan", 6)
petaJawaTengah.tambahkanJalan("Rembang","Blora", 9)
petaJawaTengah.tambahkanJalan("Jepara","Demak", 5)
petaJawaTengah.tambahkanJalan("Blora","Sragen", 30)
petaJawaTengah.tambahkanJalan("Blora","Grobogan", 54)
petaJawaTengah.tambahkanJalan("Salatiga","Grobogan", 24)
petaJawaTengah.tambahkanJalan("Salatiga","Boyolali", 74)
petaJawaTengah.tambahkanJalan("Grobogan","Sragen", 45)
petaJawaTengah.tambahkanJalan("Grobogan","Demak", 55)
petaJawaTengah.tambahkanJalan("Grobogan","Semarang", 11)
petaJawaTengah.tambahkanJalan("Grobogan","Boyolali", 23)
petaJawaTengah.tambahkanJalan("Temanggung","Salatiga", 33)
petaJawaTengah.tambahkanJalan("Temanggung","Boyolali", 32)

petaJawaTengah.printPeta()
jarakterpendek = petaJawaTengah.dijkstra("Kudus")
print("Jarak terpendek dari kota Kudus ke kota yang lain:")
for city, distance in jarakterpendek.items():
    print(city, ":", distance)
shortest_path, shortest_distance = petaJawaTengah.tsp()
print("Shortest TSP path:", shortest_path)
print("Shortest TSP distance:", shortest_distance)