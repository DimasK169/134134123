class decryption :

    def dekrip(kalimat):
        kalimat = kalimat.lower()
        hasil_encode = ''
        for karakter in kalimat:
            if karakter in abjad:
             index_lama = abjad.index(karakter)
             index_baru = (index_lama + -8 ) % len(abjad)
             abjad_baru = abjad[index_baru]
             hasil_encode = hasil_encode + abjad_baru 
            else:
             hasil_encode = hasil_encode + ' ' 
        return hasil_encode
