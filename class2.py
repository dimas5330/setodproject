import class1
show = class1.panggil()
class panggil2:
    """description of class"""
    
    def menu(self):
        Keyword1 = input('Silahkan Ketik "Keyword" untuk menampilkan keyword dalam aplikasi ini : ')
        while (Keyword1 != 'Keyword'):
            show.warning_wrongKeyword()
            Keyword1 = input('Silahkan Ketik "Keyword" untuk menampilkan keyword dalam aplikasi ini : ')
        while (Keyword1 == 'Keyword'):
           show.Keyword()
           i=1
           if i == 1:
               break
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
                    break
        elif (Keyword2 == 'Syestem'):
            show.System()
        elif (Keyword2 == 'Bandwidth'):
            show.Bandwidth()
        elif (Keyword2 == 'Bandwidth Counter'):
            show.Bandwidth_counter()
        elif (Keyword2 == 'Channel'):
            show.Channel()
        else:
            print('Keyword Salah\nUlang kembali!!')