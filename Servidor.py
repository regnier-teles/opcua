from mimetypes import init
from opcua import Server
from threading import Thread 
from time import sleep
import socket
import os


os.system('cls' if os.name == 'nt' else 'clear')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))

ip_OPC = str(s.getsockname()[0])
porta_OPC = '4840'

#
servidor = Server()
servidor.set_endpoint(f'opc.tcp://{ip_OPC}:{porta_OPC}')

spaceNome = 'Flexsim'
space = servidor.register_namespace(spaceNome)

objetos = servidor.get_objects_node()
grupo_objetos = objetos.add_object(space, 'Grupo Objetos')

estado01 = grupo_objetos.add_variable(space, 'Estado 01', 0)
estado02 = grupo_objetos.add_variable(space, 'Estado 02', 1)
estado03 = grupo_objetos.add_variable(space, 'Estado 03', 2)
estado04 = grupo_objetos.add_variable(space, 'Estado 04', 3)
estado05 = grupo_objetos.add_variable(space, 'Estado 05', 4)

estado01.set_writable()
estado02.set_writable()
estado03.set_writable()
estado04.set_writable()
estado05.set_writable()

servidor.start()

'''try:
    x1 = estado01.get_value()
    x2 = estado02.get_value()
    x3 = estado03.get_value()
    x4 = estado04.get_value()
    x5 = estado05.get_value()
    count = 1
    while True:
        estado_atual_01 = estado01.get_value()
        estado_atual_02 = estado02.get_value()
        estado_atual_03 = estado03.get_value()
        estado_atual_04 = estado04.get_value()
        estado_atual_05 = estado05.get_value()

        if count == 1: 
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'Endereço: {ip_OPC}:{porta_OPC}')
            print(f'Estado 01: {estado_atual_01}')
            print(f'Estado 02: {estado_atual_02}')
            print(f'Estado 03: {estado_atual_03}')
            print(f'Estado 04: {estado_atual_04}')
            print(f'Estado 05: {estado_atual_05}')
            count = 0
        if estado_atual_01 != x1 :
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'Endereço: {ip_OPC}:{porta_OPC}')
            print(f'Estado 01: {estado_atual_01}')
            print(f'Estado 02: {estado_atual_02}')
            print(f'Estado 03: {estado_atual_03}')
            print(f'Estado 04: {estado_atual_04}')
            print(f'Estado 05: {estado_atual_05}')
            x1 = estado_atual_01
                                
        if estado_atual_02 != x2 :
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'Endereço: {ip_OPC}:{porta_OPC}')
            print(f'Estado 01: {estado_atual_01}')
            print(f'Estado 02: {estado_atual_02}')
            print(f'Estado 03: {estado_atual_03}')
            print(f'Estado 04: {estado_atual_04}')
            print(f'Estado 05: {estado_atual_05}')
            x2 = estado_atual_02
        if estado_atual_03 != x3 :
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'Endereço: {ip_OPC}:{porta_OPC}')
            print(f'Estado 01: {estado_atual_01}')
            print(f'Estado 02: {estado_atual_02}')
            print(f'Estado 03: {estado_atual_03}')
            print(f'Estado 04: {estado_atual_04}')
            print(f'Estado 05: {estado_atual_05}')
            x3 = estado_atual_03
        if estado_atual_04 != x4 :
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'Endereço: {ip_OPC}:{porta_OPC}')
            print(f'Estado 01: {estado_atual_01}')
            print(f'Estado 02: {estado_atual_02}')
            print(f'Estado 03: {estado_atual_03}')
            print(f'Estado 04: {estado_atual_04}')
            print(f'Estado 05: {estado_atual_05}')
            x4 = estado_atual_04
        if estado_atual_05 != x5 :
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'Endereço: {ip_OPC}:{porta_OPC}')
            print(f'Estado 01: {estado_atual_01}')
            print(f'Estado 02: {estado_atual_02}')
            print(f'Estado 03: {estado_atual_03}')
            print(f'Estado 04: {estado_atual_04}')
            print(f'Estado 05: {estado_atual_05}')
            x5 = estado_atual_05
        
finally:
    servidor.stop()'''