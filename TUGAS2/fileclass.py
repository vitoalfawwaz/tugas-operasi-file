class HandleFile:
    def __init__(self):
        pass

    def baca_file(self, nama_file):
        try:
            with open(nama_file, 'r') as file:
                isi_file = file.read()
                print(isi_file)
        except FileNotFoundError:
            print(f"File {nama_file} tidak ditemukan.")
        except Exception as e:
            print(f"Terjadi kesalahan saat membaca file: {e}")

    def tulis_file(self, nama_file, mode):  
        try:
            nama_pemainMU = input("Nama Pemain MU: ")
            teks = "\n {}".format(nama_pemainMU)
            with open(nama_file, mode) as file:
                file.write(teks)
                print(f"Text sudah disimpan di file {nama_file}")
        except Exception as e:
            print(f"Menulis gagal: {e}")