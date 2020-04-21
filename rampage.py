import class1
show = class1.panggil()

def return_func(welcome):
    return print(welcome)


return_func('Selamat Datang di Aplikasi RAMpage \nAplikasi untuk mengenal lebih dalam tentang RAM')
Keyword1 = input('Silahkan Ketik keyword untuk menampilkan keyword dalam aplikasi ini : ')
while (Keyword1 != 'Keyword'):
    show.warning_wrongKeyword()
    Keyword1 = input('Silahkan Ketik keyword untuk menampilkan keyword dalam aplikasi ini : ')
if Keyword1 == 'Keyword':
   show.Keyword()
Keyword2 = input('Silahkan masukkan Keyword untuk memakai aplikasi : ')
if (Keyword2 == 'RAM'):
   show.RAM()
elif (Keyword2 == 'Spesifikasi'):
    show.spesifikasi()
    show.Rumus_ram()
    lagi = input('Apakah anda ingin menghitung lagi?(y/n)')
    while (lagi == 'y'):
        show.Rumus_ram()
        if lagi == 'n' :
            print('Terimakasih sudah menggunakan alat kami ^^')
            break
elif (Keyword2 == 'Timing'):
   show.Timing()
elif (Keyword2 == 'Impact'):
    show.Impact()
    show.Rumus_Impact()
    lagi = input('Apakah anda ingin menghitung lagi?(y/n)')
    while (lagi == 'y'):
        show.Rumus_Impact()
        if lagi == 'n' :
            print('Terimakasih sudah menggunakan alat kami ^^')
            break
elif (Keyword2 == 'Syestem'):
    show.System()
elif (Keyword2 == 'Bandwidth'):
    show.Bandwidth()
elif (Keyword2 == 'Bandwidth Counter'):
    print('Berikut adalah alat untuk menghitung Bandwidth RAM : ')
    clock = int(input('Masukkan DDR Clock Rate,bukan Real Clock Rate : '))
    Bandwidth = clock * 8
    print("Bandwidth dari RAM anda adalah : ")
    print(Bandwidth)
elif (Keyword2 == 'Channel'):
    show.Channel()

#loop menu
lagi = input('Apakah anda ingin memakai aplikasi lagi?(y/n)')
while (lagi == 'y'):
    Keyword2 = input('Silahkan masukkan Keyword untuk memakai aplikasi : ')
    if (Keyword2 == 'RAM'):
       show.RAM()
    elif (Keyword2 == 'Spesifikasi'):
        show.spesifikasi()
        show.Rumus_ram()
        while (lagi == 'y'):
            show.Rumus_ram()
            lagi = input('Apakah anda ingin menghitung lagi?(y/n)')
            if lagi == 'y':
                print('Terimakasih sudah menggunakan alat kami ^^')
                break
    elif (Keyword2 == 'Timing'):
        show.Timing()
    elif (Keyword2 == 'Impact'):
        show.Impact()
        show.Rumus_Impact()
        while (lagi == 'y'):
            show_Rumus_Impact()
            if lagi == 'n':
                print('Terimakasih sudah menggunakan alat kami ^^')
                break
    elif (Keyword2 == 'Syestem'):
       show.System()
    elif (Keyword2 == 'Bandwidth'):
        show.Bandwidth
    elif (Keyword2 == 'Bandwidth Counter'):
        print('Berikut adalah alat untuk menghitung Bandwidth RAM : ')
        clock = int(input('Masukkan DDR Clock Rate,bukan Real Clock Rate : '))
        Bandwidth = clock * 8
        print("Bandwidth dari RAM anda adalah : ")
        print(Bandwidth)
    elif (Keyword2 == 'Channel'):
        show.Channel()
    if (lagi == 'n'):
        print('Terimakasih sudah menggunakan Aplikasi kami,Jika berkenan anda boleh membantu kami dengan berdonasi seikhlasnya ke rekening : 12345678 a/n Dimas Seto ')
        break