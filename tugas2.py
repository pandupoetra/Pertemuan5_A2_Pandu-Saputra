awal=int(input("Masukan saldo awal\t:"))
sisa=awal
while(True):
    pengeluaran=int(input("Masukan pengeluaran hari ini (-1 untuk keluar):"))
    if pengeluaran==-1:
        print("Sisa saldo=",sisa)
        break
    sisa=sisa-pengeluaran
    if sisa<0:
        print("Saldo tidak cukup")
        print("“Sisa saldo",sisa+pengeluaran)
        break