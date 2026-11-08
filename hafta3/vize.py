from datetime import datetime

vize = datetime.strptime(input("Vizen ne zaman ve saat kaçta?"), "%d.%m.%Y %H:%M")
şimdi = datetime.now()

kalan = vize - şimdi

gün = kalan.days
saat = kalan.seconds // 3600

print(f"Vizenize", gün, "gün, ", saat, "saat kalmıştır.")