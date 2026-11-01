def main():
    x = int(input("Ürünün fiyatsız tutarı nedir?"))
    y = int(input("İndirim oranı kaçtır?"))

    print("Son fiyatınız", indirim_hesapla(x, y))


def indirim_hesapla(x, y):
    return x * (100 - y) / 100

main()