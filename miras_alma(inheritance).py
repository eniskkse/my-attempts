import time
class Taşıt():
    liste=[]
    def __init__(self,marka,model,km):
        self.marka=marka
        self.model=model
        self.km=km
        self.tekerlek=4
        self.fiyat(self.model,self.km)
        print(f"{marka}Taşıtı oluturuldu")
        
    def fiyat(self,model,km):
        self.listeye_ekle(self.marka)
        print("Biraz Bekleticem...")
        time.sleep(3)
        
        if (self.model>=2015) or (self.km<=30000):
            print(f"{self.marka} aracın fiyatı 200000 üzerinde")
        
        else:
            print(f"{self.marka} aracın fiyatı 200000 altında")

    @classmethod
    def listeye_ekle(cls,marka):
        
        cls.liste.append(marka)
        print("Yeni liste: ",cls.liste)

    @classmethod
    def listeden_cıkar(cls,marka):
        cls.liste.remove(marka)
        print(f"Çıkarılmış liste: {cls.liste} ")

class Motor(Taşıt):
    motorlist=[]
    def __init__(self,marka,model,km):
        super().__init__(marka,model,km)
        self.teker=2

    @classmethod
    def listeye_ekle(cls,marka):
        
        cls.motorlist.append(marka)
        print("Yeni liste: ",cls.motorlist)

    @classmethod
    def listeden_cıkar(cls,marka):
        cls.motorlist.remove(marka)
        print(f"Çıkarılmış liste: {cls.motorlist} ")

class Bisiklet():
    bisikletlist=[]
    def __init__(self,marka,maşa,tür,fren):
        self.marka=marka
        self.maşa=maşa
        self.tür=tür
        self.fren=fren
        self.tekerlek=2
        self.listeye_ekle(self.marka)
        self.özellik_göster()

    @classmethod
    def listeye_ekle(cls,marka):
        cls.bisikletlist.append(marka)
        print(f"Yeni bisiklet listesi: {cls.bisikletlist}")

    @classmethod
    def listeden_cıkar(cls,marka):
        cls.bisikletlist.remove(marka)
        print(f"{marka} çıkarılmış eksilen liste: {cls.bisikletlist}")

    def özellik_göster(self):
        print(f"{self.marka}'nın özelikleri:{self.maşa,self.tür,self.fren} ")
    
m1=Motor("yamaha",2005,20000)
t1=Taşıt("Audi",2020,0)
m2=Motor("suzuki",1998,50000)
Motor.listeden_cıkar("yamaha")
b1=Bisiklet("kron","kitlenebilir","şehir bisikleti","hidrolik")