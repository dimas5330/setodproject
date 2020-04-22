import class2
show = class2.panggil2()

def return_func(welcome):
    return print(welcome)

return_func('Selamat Datang di Aplikasi RAMpage \nAplikasi untuk mengenal lebih dalam tentang RAM')
show.menu()

#loop menu
lagi = input('Apakah anda ingin memakai aplikasi lagi?(y/n) : ')
while (lagi == 'y'):
    show.menu()
    lagi = input('Apakah anda ingin memakai aplikasi lagi?(y/n) : ')
while (lagi == 'n'):
    print('Terimakasih sudah menggunakan Aplikasi kami,Jika berkenan anda boleh membantu kami dengan berdonasi seikhlasnya ke rekening : 12345678 a/n Dimas Seto ')
    break
while (lagi != 'y' and lagi != 'n'):
    print ('Input salah, Aplikasi berhenti!!')
    break