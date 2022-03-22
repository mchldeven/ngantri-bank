teller1 = []
teller2 = []
teller3 = []
nasabah = []
ruang_tunggu = []


def menu():
    # import os
    # os.system("cls")

    print("="*50)
    print("\t\t TAMPILAN MENU DEVLOPED BY MICHAEL DEVEN ")
    print("="*50)
    print("1. Input Antrian")
    print("2. Cek Teller")
    print("3. Ruang Tunggu")
    print("4. Antrian Yang Sudah Selesai")
    print("5. Info Antrian")
    print("6. Keluar")
    print()
    try:
        pilih_menu = int(input("Pilih Menu : "))
        if pilih_menu == 1:
            input_antrian()
        elif pilih_menu == 2:
            cek_di_teller()
        elif pilih_menu == 3:
            info_ruang_tungu()
        elif pilih_menu == 4:
            print("BELUM DIBUAT")
        elif pilih_menu == 5:
            info_antrian()
        elif pilih_menu == 6:
            print("Keluar")
        else:
            print()
            print("ERROR: Pilihan tidak tersedia")
            menu()
    except ValueError:
        print()
        print(
            "ERROR : Harap Input Ulang Dengan Format ANGKA/NOMOR! Jangan Memasukkan Input KOSONG, HURUF, atau SIMBOL")
        print()
        menu()


# def tanya_menu():
#     print()
#     print("Ingin Kembali ke Menu ? (1.Ya/2.Tidak)")
#     try:
#         kembali = int(input(">>> "))
#         if kembali == 1:
#             menu()
#         elif kembali == 2:
#             re
#         else:
#             print()
#             print("Error : Pilihan Salah. Silahkan Input ANGKA/NOMOR")
#             tanya_menu()
#     except ValueError:
#         print()
#         print("ERROR : Input Yang Dimasukkan Salah. Harap Memasukkan Ulang ANGKA/NOMOR Jangan Memasukkan Huruf, Kosong, atau Simbol")
#         tanya_menu()


def input_antrian():
    nomor_antrian = 0
    tambah = input()
    if tambah:
        asa
    nasabah.append(nona)
    print(nona)
    print(nasabah)
    lent1 = len(teller1)
    lent2 = len(teller2)
    lent3 = len(teller3)

    # if lent1 == 0:
    #     print('Nasabah No {} harap menuju Teller 1 '.format(nona))
    #     input('Tekan [ENTER] Untuk Kembali Ke Menu ')
    #     teller1.append(nasabah[-1])
    #     menu()
    # elif lent2 == 0:
    #     print('Nasabah No {} berada di Teller 2 '.format(nona))
    #     input('Tekan [ENTER] Untuk Kembali Ke Menu ')
    #     teller2.append(nasabah[-1])
    #     menu()
    # elif lent3 == 0:
    #     print('Nasabah No {} berada di Teller 3 '.format(nona))
    #     input('Tekan [ENTER] Untuk Kembali Ke Menu ')
    #     teller3.append(nasabah[-1])
    #     menu()
    # else:
    #     print("Semua Teller Penuh, Harap Menunggu")
    #     ruang_tunggu.append(nasabah[-1])
    #     menu()
    # found = False
    # try:
    #     antrian = int(input("Masukkan antrian baru : "))
    #     if antrian in nasabah:
    #         found = True
    #         print("Nomor Antrian Sudah Ada. Harap Input Nomor Antrian Baru")
    #         input_antrian()
    #     else:
    #         nasabah.append(antrian)
    #         input_teller()
    # except ValueError:
    #     print()
    #     print("ERROR : Harap Input Ulang Dengan Format ANGKA/NOMOR! Jangan Memasukkan Input KOSONG, HURUF, atau SIMBOL")
    #     print()
    #     input_antrian()

    # input_teller()

    # nasabah.append(antrian)
    # input_teller()


def input_teller():
    print("Silahkan Pilih Teller :")
    print("1. Teller-1")
    print("2. Teller-2")
    print("3. Teller-3")

    try:
        pilih_teller = int(input("Pilih Teller : "))
        if pilih_teller == 1:
            cek_teller1()
        elif pilih_teller == 2:
            cek_teller2()
        elif pilih_teller == 3:
            cek_teller3()
        else:
            print()
            print("ERROR : Pilihan Tidak Tersedia. Silahkan Input Ulang!")
            input_teller()
    except ValueError:
        print()
        print("ERROR : Harap Input Ulang Dengan Format ANGKA/NOMOR! Jangan Memasukkan Input KOSONG, HURUF, atau SIMBOL")
        print()
        input_teller()


def cek_teller1():
    print("-"*30, "INFO TELLER", "-"*30)

    if len(teller1) == 0:
        teller1.append(nasabah[-1])
        print()
        print("-"*50)
        print(
            "\t Nasabah ke-{}".format(nasabah[-1]), "Harap Menuju Ke TELLER 1")
        print("-"*50)
        print()
    else:
        print()
        print("-"*60)
        print("\t\t Terdapat Nasabah di TELLER 1")
        print(
            "\t   Silahkan Nasabah ke-{} Diharap Menunggu".format(nasabah[-1]))
        print("-"*60)
        print()
        ruang_tunggu.append(nasabah[-1])

    print("Tekan [ENTER] Untuk Kembali Ke MENU ")
    input()
    menu()


def cek_teller2():
    if len(teller2) == 0:
        teller2.append(nasabah[-1])
        print()
        print("-"*50)
        print(
            "\t Nasabah ke-{}".format(nasabah[-1]), "Harap Menuju Ke TELLER 2")
        print("-"*50)
        print()
    else:
        print()
        print("-"*60)
        print("\t\t Terdapat Nasabah di TELLER 2")
        print(
            "\t   Silahkan Nasabah ke-{} Diharap Menunggu".format(nasabah[-1]))
        print("-"*60)
        print()
        ruang_tunggu.append(nasabah[-1])

    print("Tekan [ENTER] Untuk Kembali Ke MENU ")
    input()
    menu()


def cek_teller3():
    print()
    print()
    if len(teller3) == 0:
        teller3.append(nasabah[-1])
        print()
        print("-"*50)
        print(
            "\t Nasabah ke-{}".format(nasabah[-1]), "Harap Menuju Ke TELLER 3")
        print("-"*50)
        print()
    else:
        print()
        print("-"*60)
        print("\t\t Terdapat Nasabah di TELLER 3")
        print(
            "\t   Silahkan Nasabah ke-{} Diharap Menunggu".format(nasabah[-1]))
        print("-"*60)
        print()
        ruang_tunggu.append(nasabah[-1])

    print("Tekan [ENTER] Untuk Kembali Ke MENU ")
    input()
    menu()


def cek_di_teller():
    print()
    print("-"*14, " INFO TELLER ", "="*14)
    print("TELLER 1 : ", *teller1)
    print("TELLER 2 : ", *teller2)
    print("TELLER 3 : ", *teller3)
    print("-"*43)
    print()

    print("Tekan [ENTER] Untuk Kembali Ke MENU ")
    input()
    menu()


def info_ruang_tungu():
    print()
    print("-"*14, " Ruang Tunggu ", "="*14)
    print("Terdapat Nasabah Dengan Nomor Antrian : ", *ruang_tunggu)
    print("-"*45)
    print()

    print("Tekan [ENTER] Untuk Kembali Ke MENU ")
    input()
    menu()


def info_antrian():
    print()
    print("-"*14, " INFO ANTRIAN BANK ", "-"*14)

    if len(nasabah) == 0:
        print("Data Antrian Kosong")
        print("Data tidak dapat ditampilkan")
    else:
        print("RUANG TUNGGU | Nomor Antrian : ", *ruang_tunggu)
        print("TELLER 1     | Nomor Antrian : ", *teller1)
        print("TELLER 2     | Nomor Antrian : ", *teller2)
        print("TELLER 3     | Nomor Antrian : ", *teller3)

    print("-"*49)
    print()

    print("Tekan [ENTER] Untuk Kembali Ke MENU ")
    input()
    menu()


menu()

#  class Queue():
#      def __init__(self) -> None:
#          self.