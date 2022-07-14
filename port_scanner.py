
import socket
import time



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


target = input('Ingresa la IP a reconocer: ')


target_ip = socket.gethostbyname(target)
print('Iniciando reconocimiento de puertos de la IP', target_ip)


def port_scan(port):
    try:
        s.connect((target_ip, port))
        return True
    except:
        return False

start = time.time()

for port in range(65535):
    if port_scan(port):
        print(f'El Puerto {port} esta ABIERTO')
    else:
        a=1

end = time.time()
print(f'Realizado en {end-start:.2f} segundos')
