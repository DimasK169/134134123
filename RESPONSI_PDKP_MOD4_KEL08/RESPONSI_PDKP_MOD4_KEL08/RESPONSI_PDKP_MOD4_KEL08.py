import decryption

abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

key = 8

print("Enkripsi = 1")
print("Dekripsi = 2")
kode = int(input("Masukkan fungsi yang ingin digunakan :"))

def encode(kalimat,cipher_key):
  kalimat = kalimat.lower()
  hasil_encode = ''
  for karakter in kalimat:
    if karakter in abjad:
      index_lama = abjad.index(karakter)
      index_baru = (index_lama + cipher_key ) % len(abjad)
      abjad_baru = abjad[index_baru]
      hasil_encode = hasil_encode + abjad_baru 
    else:
       hasil_encode = hasil_encode + ' ' 
  return hasil_encode

kalimat = input('Masukkan kalimat :  ')

if kode == 1 :
    kalimat_hasil = encode(kalimat,key)
    print('Hasil enkripsi kalimat adalah : ', kalimat_hasil)
elif kode == 2 : 
    kalimat_hasil = encode(kalimat,-key)
    dekrip = decryption.decryption
    kalimat_awal = dekrip()
    print('Hasil dekripsi kalimat adalah : ', kalimat_hasil)

