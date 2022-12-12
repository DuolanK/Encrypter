import pyAesCrypt
from getpass import getpass

password = getpass(prompt='Input your pass: ')

#encrypt
#pyAesCrypt.encryptFile('data.txt', 'data.txt.aes', password)

#decrypt
pyAesCrypt.decryptFile('data.txt.aes', 'dataout.txt', password)