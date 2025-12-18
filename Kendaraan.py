class Kendaraan:
    def __init__(self, merk):
        self.merk = merk

    def info(self):
        print("Merk kendaraan:", self.merk)

    def pembayaran(self):
        print("pembelian motor")

class Motor(Kendaraan):
    def jalan(self):
        print("Motor berjalan")

    def parkiran(self):
        print("motor berhenti")

m = Motor("Honda")
m.pembayaran()
m.info()
m.jalan()
m.parkiran()
