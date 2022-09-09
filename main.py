import time
import socket
import smtplib
import socket
import os
import sys
print('')

restart = 'S'

while restart == 'S':
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    time.sleep(0.5)
    os.system("figlet  DNS and IP")
    time.sleep(0.5)
    print('Tool by tekashiZiinMaKer')
    time.sleep(0.5)
    time.sleep(0.5)
    print('Checking updates...')
    os.system('clear')
    os.system("figlet  Consulta DNS")
    time.sleep(2)
    print()

    print('[1] Query IP de Hosts')
    print('[2] by tekashi')

    def host():
        print('')
        print('Olá!')
        time.sleep(0.3)
        print('Aqui, você pode pegar endereçamentos de específicos hostnames.\n')
        time.sleep(0.5)
        host = input('Consulte uma DNS: ')
        host = socket.gethostname()
        intern = socket.gethostbyname(host)
        extern = get('https://api.ipify.org').text
        print()

        print(f'Host: {host}')
        print(f'IP Interno: {intern}')
        print(f'IP Externo: {extern}')

    def help():
        print('não kibe seu filha da puta, demorou pra fazer, pelo menos da os créditos!')

    mid = input("\n>>> Choose options: ")

    if mid == '1':
        host()

    elif mid == '2':
        help()

    restart = str(input('\nDeseja realizar outra consulta S/N? ')).strip().upper()[0]
    print('')
    os.system('cls')
