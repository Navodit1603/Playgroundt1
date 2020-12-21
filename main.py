print("Navodit's Binary and Decimal Calculator")
print("1. Binary to Decimal")
print("2. Decimal to Binary")
c = int(input("What is your choice:"))

if c == 1:
    import bin2dec
    bin2dec.bin2dec()


if c == 2:
    import dec2bin
    dec2bin.dec2bin()