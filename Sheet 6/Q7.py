encoded_password = 'K8$%j'
decoded_password = ''.join(str(ord(char)) for char in encoded_password)
print(decoded_password)
