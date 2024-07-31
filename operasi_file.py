def membaca():
    with open('file.txt', "r") as file_txt:
        file_content = file_txt.read()
        print(file_content)

def menulis():
    
    membaca()

    nama_pemain = input("Nama pemain Manchester United: ")
    text = "\n {}".format(nama_pemain)


    with open("file.txt", "a") as file_anime:
        file_anime.write(text)

menulis()