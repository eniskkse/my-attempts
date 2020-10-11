import webbrowser as wb
import os
import math
import random
import sys
import subprocess as sb
soru=print("Yapay zeka denemeleri\
 !!!Nasıl yardımcı olabilirim?")
num=random.randrange(0,100)

girdi=input()


def islem(işlem1):
    
    print(eval(işlem1))

def calistir(a):
   
    sb.call(a)

def oyun():
    global num
    while True:
        guess=int(input("Tahmininiz?"))
        if guess<num:
            print("Yukarı çık")
            return guess
        elif num<guess:
            print("Aşağı in")
            return guess
        elif num==guess:
            print("Tebrikler sayıyı buldunuz")
            return
    
def web(girdi):
    wb.open_new_tab(girdi)
    exit()
####Decider###
while bool(girdi):
    def brain(girdi):
        if girdi=="işlem":
            işlem1=input("İşleminiz?")
           
            islem(işlem1)
            return girdi

        elif girdi=="oyun":
            oyun()
            return girdi

        elif girdi=="çalıştır":
            işlem1=input("Çalıştırmak istediğiniz program nedir?")
            calistir(işlem1)
            return girdi
        else:
            print("Ne demek istediğinizi anlayamadım.")
            return web(girdi)
            
    brain(girdi)
