def baca_file(nama_file):
    with open(nama_file, "r") as file_txt:
        file_content = file_txt.read()
        print(file_content)

def tulis_file(nama_file):
    
    baca_file("file.txt")

    nama_pemain = input("Nama Pemain Manchester United: ")
    text = "\n {}".format(nama_pemain)


    with open('file.txt', "a") as file_pemain:
        file_pemain.write(text)

tulis_file("file.txt")