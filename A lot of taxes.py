taxes = int(input("Introduce your income\n"))
if taxes < 100000:
    print("5% taxes")
elif taxes >= 100000 and taxes < 200000:
    print("15% taxes")
elif taxes >= 200000 and taxes < 350000:
    print("20% taxes")
elif taxes >= 350000 and taxes < 600000:
    print("30% taxes")
elif taxes >= 600000:
    print("45% taxes")