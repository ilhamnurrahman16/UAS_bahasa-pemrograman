
import getpass

def login():
    print("============================================")
    print("\n\t---pilihan---")
    print("\t1. penilaian")
    print("\t2. pembayaran")
    print("\t3. kalkulator")

    pilih = input("\n\tsilakan pilih : ")
    if pilih == "1":
        from perhitungan.penilaian import tt
    elif pilih == "2":
        from perhitungan.pembayaran import pembayaran
    elif pilih == "3":
        from perhitungan.kalkulator import menu
    else:
        exit
    tanya()

def tanya():
    tanya = input("nKembali ke menu (y/t)? ")
    if tanya == "y":
        login()
    elif tanya == "t":
        exit
    else:
        print ("\n\tSalah input...........!!!!")

username = input("\nUsername : ")
password = getpass.getpass()
print("===============================================")

if username == "ilham" and password == "115":
    login()
    
else:
    print ("maaf password atau username mu salah.....!!!")
    
