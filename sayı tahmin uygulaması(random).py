import random
num=random.randint(1,100)
hak=int(input("Kaç hak istersiniz"))

while True:
    result=int(input("Tahmininiz?"))
    if num<result:
        hak-=1
        print(f"aşağı in! Kalan hak sayınız:{hak}")
        if hak==0:
            print("Hakkınız bitti")
        
    elif num>result:
        hak-=1
        print(f"yukarı çık! Kalan hak sayınız:{hak}")
        if hak==0:
            print("Hakkınız bitti")
            
            
    else:
        print("sayıyı buldunuz")
