# Class induk
class Kendaraan:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun

    def info(self):
        print(f"Merk: {self.merk}")
        print(f"Tahun: {self.tahun}")


# Class turunan
class Mobil(Kendaraan):
    def __init__(self, merk, tahun, jumlah_pintu):
        # Memanggil constructor dari class induk
        super().__init__(merk, tahun)
        self.jumlah_pintu = jumlah_pintu

    def jalan(self):
        print(f"Mobil {self.merk} sedang berjalan.")

    def info(self):
        # Override method
        super().info()
        print(f"Jumlah pintu: {self.jumlah_pintu}")


# Membuat object
mobil1 = Mobil("Toyota", 2022, 4)

# Mengakses method
mobil1.info()
mobil1.jalan()