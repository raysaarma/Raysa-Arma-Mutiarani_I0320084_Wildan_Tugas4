Kg = 0.453592
beratMaxKg = 50*Kg

while True:
    print('Berat maksimum bagasi : {} kg'. format(beratMaxKg))
    beratKg = float(input('Masukkan berat bagasi anda dalam Kg: '))
    if beratKg >= beratMaxKg :
        status = False
        if beratKg > 110 :
            print('Berat bagasi anda adalah', beratKg, 'Kg, Lebih dari 110 Kg :', status)
        elif beratKg == 49 :
            print('Berat bagasi anda adalah', beratKg, 'Kg :', status)
        else :
            print('Berat bagasi anda adalah', beratKg, 'Kg, melebihi batas muatan :', status)
    else :
        status = True
        print('Berat bagasi anda adalah', beratKg, 'Kg, masih dibawah batas muatan :', status)
    print('='*100)
