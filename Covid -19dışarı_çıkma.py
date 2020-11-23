import datetime
import time


class A():
    print("""Dışarı çıkabilirmiyim uygulaması""")
    
    def __init__(self):
        self.girdi=int(input("Yaşınıızı giriniz"))
        self.days=("Monday","Tuesday","Wednesday","Thursday","Friday")
        self.son=("Saturday","Sunday")
        self.x = datetime.datetime.now()
        self.day=self.x.strftime("%A")
        self.z=int(self.x.strftime("%H"))
        self.y=(self.day in self.days) and (self.girdi<=20)
        self.q=(self.day in self.days) and (20<self.girdi<=65)
        self.w=(self.day in self.days) and (self.girdi>=65)
        self.p=(self.day in self.son) and (self.girdi<=20)
        self.o=(self.day in self.son) and (20<self.girdi<=65)
        self.ı=(self.day in self.son) and (self.girdi>=65)
        self.ss=(self.y and (13<=self.z<=16)) or (self.p and (13<=self.z<=16))#çıkan çocuk
        self.sss=(self.y and (not 13<=self.z<=16)) or (self.p and (not 13<=self.z<=16))#çıkamayan çocuk
        self.mm=((self.q) or (self.o and (10<=self.z<=20)))#çıkan yetişkin
        self.mmm=self.o and (not 10<=self.z<=20)#çıkamayan yetişkin
        self.ll=(self.w and (10<=self.z<=13)) or (self.ı and (10<=self.z<=13))#çıkan yaşlı
        self.lll=(self.w and (not 10<=self.z<=13)) or (self.ı and (not 10<=self.z<=13))#çıkamayan yaşlı
        self.işlem(self.girdi)

    def işlem(self,girdi):
        
        if self.ss:
            print("Dışarı çıkabilirsin çocuk!")
            return self.__init__()
        if self.sss:
            print("Dışarı çıkamazsın çocuk!!!")
            return self.__init__()
        if self.mm:
            print("Dışarı çıkabilirsin yetişkin!")
            return self.__init__()
        if self.mmm:
            print("Dışarı çıkamazsın yetişkin!!!")
            return self.__init__()
        if self.ll:
            print("Dışarı çıkabilirsin yaşlı!")
            return self.__init__()
        if self.lll:
            print("Dışarı çıkamazsın yaşlı")
            return self.__init__()
        
a1=A()
a1

