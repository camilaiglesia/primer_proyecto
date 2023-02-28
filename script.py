import sys
import json

argumentos = sys.argv

if len(argumentos) != 4:                        #validaciones
    print("por favor enviame los argumentos correctos")
    
else:
    print(f"Bienvenido {argumentos[1]}")
    print(type(argumentos[3]))
    lista = json.loads(argumentos[3]) #casteo. lo transformo a json y json loads (lo transforma a lista)
    print(type(lista))   
    print(lista)
    
