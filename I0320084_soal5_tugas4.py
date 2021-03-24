s = 'Strings arrange come'
print('panjang dari s = %d' %len(s))
print('kemunculan huruf pertama a = %d' %s.index('a'))
print('a muncul sebanyak %d kali' %s.count('a'))
print("lima karakter pertama adalah '%s'" %s[:5])
print("lima karakter berikutnya adalah '%s'" %s[5:10])
print("lima karakter ketiga belas adalah '%s'" %s[12])
print("karakter dengan indeks ganjil adalah '%s'" %s[1::2])
print("lima karakter terakhir adalah '%s'" %s[-5:])
print('string dalam huruf besar: %s' %s.upper())
print('string dalam huruf kecil: %s' %s.lower())
if s.startswith('Str'):
    print("string dimulai dengan 'Str'. Good!")
if s.endswith('ome'):
    print("string diakhiri dengan 'ome'. Good!")
print('pisahkan kata-kata dari string tersebut: %s' %s.split(" "))