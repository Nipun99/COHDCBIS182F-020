----Code for Encrypting----

plaintext = input('Enter Message :')
alphabet="abcdefghijklmnopqrstuvwxyz"
key=1
cipher=''

for c in plaintext:
    if c in alphabet:
          cipher += alphabet [(alphabet.index(c) +key)%(len (alphabet))]
print('your encrypted message is :' + cipher)



----Code for Decrypting----

plaintext = input('Enter Message :')
alphabet="abcdefghijklmnopqrstuvwxyz"
key=1
cipher=''

for c in plaintext:
    if c in alphabet:
          cipher += alphabet [(alphabet.index(c) -key)%(len (alphabet))]
print('your encrypted message is :' + cipher)
