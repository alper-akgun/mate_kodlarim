from random import randint

x = randint(0,100)

while True:
    n = int(input("Bir sayı girin. "))
    if x < n:
        print("Aşağı in.")
    
    elif x > n:
        print("Yukarı çık.")
    
    else:
        break
print("Tebrikler sayıyı doğru tahmin ettiniz.")