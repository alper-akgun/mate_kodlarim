def main():
    v = int(input("Vize notunuz nedir?"))
    f = int(input("Final notunuz nedir?"))

    print("Harf notunuz", harf_notu_hesapla(v, f))

def ort(v, f):
        return 0.6 * v + 0.4 * f

def harf_notu_hesapla(v, f): 
    if ort(v, f) >= 90:
        return "AA"
    if ort(v, f) >= 80:
        return "BA"
    if ort(v, f) >= 70:
        return "BB"
    if ort(v, f) >= 60:
        return "CB"
    if ort(v, f) >= 50:
        return "CC"
    if ort(v, f) >= 40:
        return "DC"
    if ort(v, f) >= 30:
        return "DD"
    else:
        return "FF"

main()