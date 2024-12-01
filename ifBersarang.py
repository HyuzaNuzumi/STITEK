nm = input("Nama Karyawan:")
nk = input("Nik karyawn:")
ss = input("Status(sf/hr):")
go = input("Golongan(A/B/C):")
#nm = nama
#nk = nik
#ss = stastus
#sf = staff
#hr = honorer
#go = golongan
#ai = gaji
#bn = bonus
#gt = gaji total
if (ss == "sf"):
    ai= 1000000
    if (go == "A"):
        bn = 200000
    elif (go == "B"):
        bn = 400000
    elif (go == "C"):
        bn = 550000
elif(ss == "hr"):
    ai = 750000
    if (go == "A"):
        bn = 15000
    elif (go == "B"):
        bn = 275000
    elif (go == "C"):
        bn = 480000

gt= (ai +bn)
print("Gaji Rp.",ai)
print("Bonus Rp.",bn)
print("Gaji Total.",gt)