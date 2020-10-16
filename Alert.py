import datetime
import locale
locale.setlocale(locale.LC_ALL, 'turkish')

class Alarm():
    answer=[]

    def __init__(self):
        self.hour=int(input("Alarm kurmak istediğiniz\
saati ve tarihi yazınız.\n"))
        self.minute=int(input())
        self.nowtime=datetime.datetime.now()
        self.ask_ques()
        
    
    def ask_ques(self):
        return self.calıstır(self.hour,self.minute)
    
    @classmethod
    def repeat(cls):
        while not bool(cls.answer):
            cls.answer=input()
            print("Uyan!!!"+30*"\a")
            #Bu kısımda kullanıcı herhangi bir
            #girdi yapana dek uyandırma sesi
            #ve mesajı vermeyi sağlıyoruz


    def calıstır(self,hour,minute):
        if (self.nowtime.hour==self.hour) and (self.nowtime.minute==self.minute):
            return Alarm().repeat()
        else:
            self.calıstır(self.hour,self.minute)
    

a1=Alarm()

