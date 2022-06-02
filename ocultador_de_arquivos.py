import ctypes

#pasta = input("digite o caminho da pasta a ser ocultada: ")

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('ocultar.txt', atributo_ocultar)

if retorno:
    print("arquivo foi ocultado")
else:
    print('Arquivo não foi ocultado')
