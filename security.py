
def encrypt(password):

    password_bytes = bytes(password, "ascii")
    numberlist = ' '.join(["{0:b}".format(x) for x in password_bytes])

    xor_cipher = "00011011"
    encrypted_password = ""
    print(numberlist)
    i = -1
    for i in range:
        for ch in numberlist:
            i += 1
            if i > 7:
                i = 0
                
            if ch == "1":
                if xor_cipher[i] == "1":
                    ch = 0
                else:
                    ch = 1
            elif ch == "0":
                if xor_cipher[i] == "0":
                    ch = 0
                else:
                    ch = 1

            encrypted_password += str(ch)


    return encrypted_password



