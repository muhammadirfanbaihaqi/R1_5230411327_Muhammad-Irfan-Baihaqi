from tabulate import tabulate
import string
import random
class Pegawai:
    daftarpegawai = []
    def __init__(self,nik,nama,alamat) -> None:
        self._nik = nik
        self.nama = nama
        self.alamat = alamat

    @classmethod
    def tambahpegawai(cls):
        while True:
            nikstr = input("Masukkan NIK pegawai: ")
            cek = nikstr.isdigit()
            if cek == True: 
                nik = int(nikstr)
                nama = input("Masukkan Nama pegawai: ")
                alamat = input("Masukkan alamat pegawai: ")
                pegawaibaru = cls(nik,nama,alamat)
                cls.daftarpegawai.append(pegawaibaru)
                return True
            else:
                print("NIK HARUS BERUPA ANGKA")

    @classmethod
    def tampilsemuapegawai(cls):
        header = ["NIK","Nama Pegawai", "Alamat Pegawai"]
        dataUser = [[o._nik, o.nama, o.alamat] for o in cls.daftarpegawai]
        print(tabulate(dataUser, headers=header, tablefmt="grid"))

    @classmethod
    def tambahtransaksi(cls):
        cls.tampilsemuapegawai()
        namaPegawai = input("Masukkan nama pegawai yang membuat transaksi: ")
        for i in Pegawai.daftarpegawai:
            if namaPegawai == i.nama:
                while True:
                    Produk.tampilkanproduk()
                    produkbeli = input("SILAHKAN MASUKKAN NAMA PRODUK: ")
                    for i in Produk.daftarproduk:
                        if produkbeli == i.namaproduk:
                            # new = cls(namaPegawai, nama_produk, jumlahproduk, totalharga)
                            jumlahbeli = input("Masukan Jumlah Beli: ") #MAAF TIDAK ADA PENGECEKAN INT KARENA TERLALU PANJANG.
                            totalharga = jumlahbeli * i.harga
                            Struk(namaPegawai,produkbeli,jumlahbeli,totalharga)
                            print("Transaksi berhasil ditambahkan")
                            # lagi = input("APAKAH ADA TRANSAKSI LAIN: ")
                            # if lagi.lower() == "y":
                            #     pass
                            # else:
                            #     Transaksi.createTransaksi()
                        

                    # print("PRODUK TIDAK ADA")
                    akhiri = input("AKHIRI TRANSAKSI (Y JIKA IYA): ")
                    Transaksi.createTransaksi()
                    if akhiri.upper() == "Y":
                        return True
                    else:
                        continue

        print("Pegawai Tidak Ada")
        return True


class Transaksi:
    no_transaksi = 1
    daftartransaksi = []

    def __init__(self, detail_transaksi) -> None:
        self.no_transaksi = Transaksi.no_transaksi
        self.detail_transaksi = detail_transaksi
        Transaksi.no_transaksi += 1

    @classmethod
    def createTransaksi(cls):
        detail = input("Masukkan detail transaksi: ")
        newtransaksi = cls(detail)
        cls.daftartransaksi.append(newtransaksi)
    
    @classmethod
    def tampilsemuatransaksi(cls):
        header = ["No Transaksi","Detail Transaksi"]
        dataUser = [[o.no_transaksi, o.detail_transaksi] for o in cls.daftartransaksi]
        print(tabulate(dataUser, headers=header, tablefmt="grid"))

        

class Struk:
    daftarstruk = []

    def __init__(self, namaPegawai, nama_produk, jumlahproduk, totalharga) -> None:
        self.no_transaksi = Transaksi.no_transaksi
        self.namapegawai = namaPegawai
        self.namaproduk = nama_produk
        self.jumlahproduk = jumlahproduk
        self.totalharga = totalharga
    

    @classmethod
    def buattransaksi(cls,namaPegawai, nama_produk, jumlahproduk, totalharga):
        new = cls(namaPegawai, nama_produk, jumlahproduk, totalharga)
        cls.daftarstruk.append(new)
        return True
    
    @classmethod
    def tampilsemuastruk(cls):
        header = ["No Transaksi","Nama Pegawai", "Nama Produk", "Jumlah Produk", "Total Harga"]
        dataUser = [[o.no_transaksi, o.namapegawai, o.namaproduk, o.jumlahproduk, o.totalharga] for o in cls.daftarstruk]
        print(tabulate(dataUser, headers=header, tablefmt="grid"))


class Produk:
    daftarproduk = []
    def __init__(self,namaproduk,jenisproduk) -> None:
        self._kodeproduk = Produk.generate_id()
        self.namaproduk = namaproduk
        self.jenisproduk = jenisproduk #AKAN DIUBAH DI CHILD CLASS
    
    @staticmethod
    def generate_id():
        characters = string.ascii_letters + string.digits
        unique_id = ''.join(random.choices(characters, k=4))
        return unique_id

    # def tambahproduk(self):
    @classmethod
    def tampilkanproduk(cls):
        cls.daftarproduk.sort(key=lambda produk: produk.namaproduk.lower()) #MENGURUTKAN BERDASAR ABJAD A-Z
        header = ["Kode Produk","Nama Produk", "Jenis"]
        dataUser = [[o._kodeproduk, o.namaproduk, o.jenisproduk] for o in cls.daftarproduk]
        print(tabulate(dataUser, headers=header, tablefmt="grid"))


class Snack(Produk):
    daftarsnack = []
    def __init__(self, namaproduk,harga) -> None: #OVERRIDE
        jenisproduk = "Snack"
        super().__init__(namaproduk, jenisproduk)
        self.harga = harga

    @classmethod
    def tambahproduk(cls):
        namaproduk = input("Masukkan nama produk: ")
        while True:
            hargastr = input("Masukkan Harga Produk Satuan: ")
            cek = hargastr.isdigit()
            if cek == True:
                harga = int(hargastr)
                produkbaru = cls(namaproduk,harga)
                Produk.daftarproduk.append(produkbaru)
                cls.daftarsnack.append(produkbaru)
                print(f"produk {namaproduk}, berhasi ditambahkan")
                return True
        
    @classmethod
    def tampilkanproduk(cls): #overriding
        cls.daftarsnack.sort(key=lambda produk: produk.namaproduk.lower()) #MENGURUTKAN BERDASAR ABJAD A-Z
        header = ["Kode Produk","Nama Produk", "Jenis"]
        dataUser = [[o._kodeproduk, o.namaproduk, o.jenisproduk] for o in cls.daftarsnack]
        print(tabulate(dataUser, headers=header, tablefmt="grid"))

class Makanan(Produk):
    daftarmakanan = []
    def __init__(self, namaproduk,harga) -> None: #OVERRIDE
        jenisproduk = "Makanan"
        super().__init__(namaproduk, jenisproduk)
        self.harga = harga

    @classmethod
    def tambahproduk(cls):
        namaproduk = input("Masukkan nama produk: ")
        while True:
            hargastr = input("Masukkan Harga Produk Satuan: ")
            cek = hargastr.isdigit()
            if cek == True:
                harga = int(hargastr)
                produkbaru = cls(namaproduk,harga)
                Produk.daftarproduk.append(produkbaru)
                cls.daftarmakanan.append(produkbaru)
                print(f"produk {namaproduk}, berhasi ditambahkan")
                return True
        
    @classmethod
    def tampilkanproduk(cls): #overriding
        cls.daftarmakanan.sort(key=lambda produk: produk.namaproduk.lower()) #MENGURUTKAN BERDASAR ABJAD A-Z
        header = ["Kode Produk","Nama Produk", "Jenis"]
        dataUser = [[o._kodeproduk, o.namaproduk, o.jenisproduk] for o in cls.daftarmakanan]
        print(tabulate(dataUser, headers=header, tablefmt="grid"))

    
class Minuman(Produk):
    daftarminuman = []
    def __init__(self, namaproduk,harga) -> None: #OVERRIDE
        jenisproduk = "Minuman"
        super().__init__(namaproduk, jenisproduk)
        self.harga = harga

    @classmethod
    def tambahproduk(cls):
        namaproduk = input("Masukkan nama produk: ")
        while True:
            hargastr = input("Masukkan Harga Produk Satuan: ")
            cek = hargastr.isdigit()
            if cek == True:
                harga = int(hargastr)
                produkbaru = cls(namaproduk,harga)
                Produk.daftarproduk.append(produkbaru)
                cls.daftarminuman.append(produkbaru)
                print(f"produk {namaproduk}, berhasi ditambahkan")
                return True
        
    @classmethod
    def tampilkanproduk(cls): #overriding
        cls.daftarminuman.sort(key=lambda produk: produk.namaproduk.lower()) #MENGURUTKAN BERDASAR ABJAD A-Z
        header = ["Kode Produk","Nama Produk", "Jenis"]
        dataUser = [[o._kodeproduk, o.namaproduk, o.jenisproduk] for o in cls.daftarminuman]
        print(tabulate(dataUser, headers=header, tablefmt="grid"))

def tampilanMenuUtama():
        print("\n==============================")
        print("        MENU UTAMA        ")
        print("==============================")
        print("1. Tambah Pegawai")
        print("2. Tambah Produk")
        print("3. Tampilkan Seluruh Product")
        print("4. Tampilkan Seluruh Minuman")
        print("5. Tampilkan Seluruh Makanan")
        print("6. Tampilkann Seluruh Snack")
        print("7. Tampilkan Semua Pegawai")
        print("8. Buat Transaksi Baru")
        print("9. Tampil Semua Transaksi")
        print("10. Tampilkan Seluruh Struk")
        print("0. Exit")
        print("===============================")

def tampiltambahproduk():
    print("\n==============================")
    print("          TAMBAH PRODUK         ")
    print("==============================")
    print("1. Tambah Makanan")
    print("2. Tambah Minuman")
    print("3. Tambah Snack")
    print("4. Kembali ke menu utama")
    print("===============================")


def tambahproduk():
    while True:
        tampiltambahproduk()
        pilih = input("Masukan pilihan menu: ")
        if pilih == "1":
            Makanan.tambahproduk()
        elif pilih == "2":
            Minuman.tambahproduk()
        elif pilih == "3":
            Snack.tambahproduk()
        elif pilih == "4":
            return True
        else:
            print("Pilihan Anda salah")
            continue


def menu():
    while True:
        tampilanMenuUtama()
        pilih = input("PILIH MENU: ")
        if pilih == "1":
            Pegawai.tambahpegawai()
        elif pilih == "2":
            tambahproduk()
        elif pilih == "3":
            Produk.tampilkanproduk()
        elif pilih == "4":
            Minuman.tampilkanproduk()
        elif pilih == "5":
            Makanan.tampilkanproduk()
        elif pilih == "6":
            Snack.tampilkanproduk()
        elif pilih == "7":
            Pegawai.tampilsemuapegawai()
        elif pilih == "8":
            Pegawai.tambahtransaksi()
        elif pilih == "9":
            Transaksi.tampilsemuatransaksi()
        elif pilih == "10":
            Struk.tampilsemuastruk()
        elif pilih == "0":
            print("Anda Keluar Program")
            return True
        else:
            print("Ulang ya")

Minuman.tambahproduk()
Makanan.tambahproduk()
Pegawai.tambahpegawai()
menu()


