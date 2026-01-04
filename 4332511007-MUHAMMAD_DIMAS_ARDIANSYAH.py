'''
Enkripsi dan Dekripsi Kriptografi Caesar
'''

def encrypt(teks,geser):
    hasil = ''
    for karakter in teks:
        # Cek jika karakter adalah huruf
        if karakter.isalpha():
            # Mentukan basis karater huruf besar atau kecil
            basis = ord('A') if karakter.isupper() else ord('a')

            # Geser Karakter
            shifted_char = chr((ord(karakter) - basis + geser) % 26 + basis)
            hasil += shifted_char
        else:
            hasil += karakter
    return "Output Enkripsi Caesar = " + hasil

def decrpyt(teks,geser):
    hasil = ''
    geser = -geser

    for karakter in teks:
        # Cek jika karakter adalah huruf
        if karakter.isalpha():
            # Mentukan basis karater huruf besar atau kecil
            basis = ord('A') if karakter.isupper() else ord('a')

            # Geser Karakter
            shifted_char = chr((ord(karakter) - basis + geser) % 26 + basis)
            hasil += shifted_char
        else:
            hasil += karakter
    return "Output Dekripsi Caesar = " + hasil

def main():
    print('='*30)
    print('Kriptografi Caesar Cipher')
    print('='*30)
    print('1. Enkripsi Caesar\n2. Dekripsi Caesar\n3. Keluar')
    input_mode = input('Pilih Mode: ')
    if input_mode == '1':
        input_teks = input('Masukkan Teks : ')
        input_geser = input('Masukkan Pergeseran : ')
        print(encrypt(input_teks,int(input_geser)))
        
    elif input_mode == '2':
        input_teks = input('Masukkan Teks : ')
        input_geser = input('Masukkan Pergeseran : ')
        print(decrpyt(input_teks,int(input_geser)))
    elif input_mode == '3':
        print('Bye!')
        SystemExit
    else:
        print('Invalid Input!')
        main()

main()
