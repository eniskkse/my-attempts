class Hesapla():
    
    def __init__(self):
        self.sesli_harf="aeıioöuü"
        self.sessiz_harf="qwrtypğsdfghjklşzxcvbnmç"
        self.sayaç_sessiz=0
        self.sayaç_sesli=0

    def kelimegir(self):
        return input("Kelime giriniz")

    def sessizhes(self):
        for harf in self.kelime:
            if harf in self.sessiz_harf:
                self.sayaç_sessiz+=1
        return print(f"{self.kelime}' kelimesinin içinde,{self.sayaç_sessiz} tane sessiz harf vardır")

    def seslihes(self):
        for harf in self.kelime:
            if harf in self.sesli_harf:
                self.sayaç_sesli+=1
        return print(f"{self.kelime}' kelimesinin içinde,{self.sayaç_sesli} tane sesli harf vardır")

    def çalıştır(self):
        self.kelime=self.kelimegir()
        self.sessizhes()
        self.seslihes()

if __name__ == "__main__":

    sayaç=Hesapla()
    sayaç.çalıştır()