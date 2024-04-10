###megan enochs decoder for carolinamabad

def decoder(string):
    password = ''
    decode1 = 0
    for num in string:
        decode1 = int(num)-3
        password += string(decode1)
        decode1 = 0
    return password