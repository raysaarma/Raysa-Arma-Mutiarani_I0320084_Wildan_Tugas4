print('SYARAT MENDAFTAR KURSUS ONLINE')

while True:
    usia = int(input('Berapa usia anda? : '))
    if usia >= 21:
        kelulusan = input('Apakah anda sudah lulus ujian kualifikasi (Y/T)? : ')
        if kelulusan == 'Y':
            print('Anda dapat mendaftar di kursus')
        elif kelulusan == 'T':
            print('Anda tidak dapat mendaftar di kursus')
        else:
            print('Data yang anda masukkan salah')
    else:
        print('Anda tidak dapat mendaftar di kursus karena usia anda kurang dari 21 tahun')
    print('='*100)