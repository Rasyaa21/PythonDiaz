class LuasSegitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def hitungLuas(self):
        return 0.5 * self.alas * self.tinggi

class VolumeBalok:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def hitungVolumeBalok(self):
        return self.panjang * self.lebar * self.tinggi

class KelilingPersegi:
    def __init__(self, sisi):
        self.sisi = sisi

    def hitungKelilingPersegi(self):
        return 4 * self.sisi

# Example usage
hitungLuasSegitiga = LuasSegitiga(5, 10)
print(f"Luas Segitiga Adalah : {hitungLuasSegitiga.hitungLuas()}")

VolumeBalok1 = VolumeBalok(5, 10, 6)
print(f"Volume Balok Adalah : {VolumeBalok1.hitungVolumeBalok()}")

KelilingPersegi1 = KelilingPersegi(4)
print(f"Keliling Persegi Adalah : {KelilingPersegi1.hitungKelilingPersegi()}")
