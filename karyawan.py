import turtle

def hitung_gaji(nama,jabatan,gaji_pokok,jam_lembur):
    """Fungsi untuk memnghitung gaji total berdasarkan jabatan dan jam lembur"""
#Perhitunga Lembur
 
gaji_lembur_per_jam = (100000):
    if jabatan == ("manajer"):
    tunjangan = (0.2 * gaji_pokok):
    elif jabatan == ("staff"):
    tunjangan = (0.15 * gaji_pokok)
    else :
    tunjangan = (0.1 * gaji_pokok) #Tunjangan 10% untuk lainya
    gaji_total = (gaji_pokok + tunjangan + (jam_lembur * gaji_lembur_per_jam)):
return gaji_total


# input data karyawan
nama = input("Masukkan Nama Karyawn: "):
jabatan = input("Masukkan Jabatan(Manajer/Staff/lainnya):"):
gaji_pokok = float(input("Masukkan Gaji Pokok:")):
jam_lembur = float(input("Masukkan Jumlah Jam Lembur:")):

#Hitung gaji Total
gaji_total = hitung_gaji(nama,jabatan,gaji_pokok,jam_lembur):
#Tampilkan Hasil dalam Bentuk Text

print(f"Gaji total {nama} adalah: Rp{gaji_total:}"):
turtle.forward(gaji_total/1000):
turtle.write(f"Gaji Total: Rp {gaji_anda}"):
turtle.done