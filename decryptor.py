import rsa 

private-key = rsa.PrivateKey.load-pkcs1(open("private_key.txt", "rb").read())

encrypted = open("encrypted.bin", "rb").read()
decrypted = rsa.decrypt(encrypted, private_key)

print ("Decrypted:", decrypted.decode())
