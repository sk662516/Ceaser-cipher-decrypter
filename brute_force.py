import enchant
d=enchant.Dict("en_US")

ciphertext="G JOYGJBGTZGMK UL ZNK MKTKXGR YAHYZOZAZOUT IOVNKX OY ZNGZ HUZN YKTJKX GTJ XKIKOBKX SAYZ IUSSOZ ZNK VKXSAZKJ IOVNKX YKWAKTIK ZU SKSUXE. G IUSSUT ZKINTOWAK LUX GBUOJOTM ZNOY OY ZU AYK G QKECUXJ LXUS CNOIN ZNK IOVNKX YKWAKTIK IGT HK MKTKXGZKJ. LUX KDGSVRK, AYOTM ZNK QKECUXJ IOVNKX, CXOZK UAZ ZNK QKECUXJ LURRUCKJ HE ATAYKJ RKZZKXY OT TUXSGR UXJKX GTJ SGZIN ZNOY GMGOTYZ ZNK VRGOTZKDZ RKZZKXY"
ciphertext.upper()

words=ciphertext.split()

min_error= len(words)
key=0
for i in range(0,26):
    error=0
    for word in words:
        word = ''.join(chr((ord(letter) - ord('A') + i) % 26 + ord('A')) for letter in word)

        if (not d.check(word) and error < min_error):
            error += 1

    if min_error > error:
        key=i
        min_error=error

print("Key value is "+str(26-key))
print("Decrypted mesasge = ")
decrypted_message=""
for word in words:
    temp=""
    for letter in word:
        if letter.isalpha():
            temp += ''.join(chr((ord(letter) - ord('A') + key) % 26 + ord('A')))
        else:
            temp += letter
    decrypted_message+=temp+" "
key=26-key
print(decrypted_message)
