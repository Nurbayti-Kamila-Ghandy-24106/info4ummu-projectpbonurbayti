class Hewan:
    def makan(self):
        print("Hewan sedang makan")

    def bebek(self):
        print("hewan sedang tidur")

    def ayam(self):
        print ("hewan sedang minum")

class Kucing(Hewan):
    def suara1(self):
        print("Meong")

    def suara2(self):
        print("wekwek")

m = Motor("Honda")
m.pembayaran()
m.info()
m.jalan()
m.parkiran()
