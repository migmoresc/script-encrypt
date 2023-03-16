""" Encripta y desencripta el contenido de los archivos comunes """

import sys
import os
import base64
from cryptography.fernet import Fernet


def convierte_linea(linea, modo):
    """ Función que encripta o desencripta una cadena de texto """
    if modo == "-e":
        texto = f.encrypt(linea.encode())
    elif modo == "-d":
        texto = f.decrypt(linea)

    return texto


def desen(ficheros, modo):
    """Encripta los ficheros"""

    for fichero in ficheros:
        fichero = fichero.replace(".\\", "")
        if os.stat(fichero).st_size > 0:
            with open("#"+fichero, "w", encoding="utf-8") as fichero_nuevo:
                with open(fichero, "rb") as fichero_lectura:
                    for linea in fichero_lectura:
                        try:
                            if linea == b"\n":
                                linea = linea.decode("utf-8")
                                fichero_nuevo.write(linea)
                            else:
                                salto = 0
                                if b"\n" in linea:
                                    linea = linea[:-1]
                                    salto = 1
                                esta = False
                                for palabra in html:
                                    if palabra.encode() in linea:
                                        esta = True
                                        break
                                if esta is True:
                                    linea = linea.decode()+"\n"*salto
                                    fichero_nuevo.write(linea)
                                else:
                                    le = convierte_linea(linea, modo)
                                    fichero_nuevo.write(le.decode()+"\n")
                        except:  # pylint: disable=W0702
                            le = convierte_linea(linea, modo)
                            fichero_nuevo.write(le.decode())
                fichero_lectura.close()
            fichero_nuevo.close()
        else:
            print("El fichero está vacío")


def abrir_ficheros(ficheros, modo):
    """Encripta los ficheros"""
    for fichero in ficheros:
        fichero = fichero.replace(".\\", "")
        if os.stat(fichero).st_size > 0:
            with open("encriptado-"+fichero, "wb") as fichero_nuevo:
                with open(fichero, "r", encoding="utf-8") as fichero_lectura:
                    for linea in fichero_lectura:
                        if linea == "\n":
                            le = linea.encode("utf-8")
                            fichero_nuevo.write(le)
                        else:
                            esta = False
                            for palabra in html:
                                if palabra in linea:
                                    esta = True
                                    break
                            if esta is True:
                                le = linea.encode("utf-8")
                                fichero_nuevo.write(le)
                            else:
                                if "\n" in linea:
                                    linea = linea[:-1]
                                le = convierte_linea(linea, modo)
                                le = le + b"\n"
                                fichero_nuevo.write(le)
                fichero_lectura.close()
            fichero_nuevo.close()
        else:
            print("El fichero está vacío")


ayuda = ["-h", "--h", "/h", "-help", "--help", "/help"]
comandos = ["-e", "-d"]
html = ["DOCTYPE", "html", "head", "title", "body", "header",
        "main", "nav", "article", "aside", "footer"]

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

if (len(sys.argv) == 1 or sys.argv[1] in ayuda or sys.argv[1] not in comandos or
        len(sys.argv[3:]) == 0):
    print("""Los argumentos de este script son:
    Primer argumento: -e (encriptar) o -d (desencriptar)
    Segundo argumento: contraseña
    Siguientes argumentos: nombres de los archivos separados por espacio""")
else:
    PASW = str.encode(sys.argv[2]+("0"*(32-len(sys.argv[2]))))
    ficheros = sys.argv[3:]
    a = base64.b64encode(PASW)
    f = Fernet(a)

    if sys.argv[1] == "-e":
        abrir_ficheros(ficheros, "-e")
    else:
        desen(ficheros, "-d")

# os.remove(ficheros[0])
# os.rename("##index.html", "html")
