print('SYARAT MENDAFTAR KURSUS ONLINE')
a = int(input('Masukkan umur anda:'))
b = input('Apakah anda sudah lulus ujian kualifikasi(Y/T)? :')
if a>=21 and b == 'Y' :
    print('Anda dapat mendaftar di kursus')
else :
    print('Anda tidak dapat mendaftar di kursus')