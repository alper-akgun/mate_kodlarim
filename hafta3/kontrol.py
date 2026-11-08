while True:
    try:
        x = int(input("Bir sayı girin."))
        print(f"Sayınız {x}. ")

    except ValueError:
        print("Lütfen geçerli bir sayı giriniz.")
    else:
        break
