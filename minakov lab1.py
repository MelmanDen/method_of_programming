stroka = input()
if len(stroka) == 0 or len(stroka) > 250 or stroka.find(" ") != -1:
    quit()
else:
    decryption = list(stroka)
    n = len(stroka) // 2
    for i in range(n):
        decryption[2 * i: 2 * i + 2] = stroka[i + n], stroka[i]
    print(''.join(decryption))
quit()