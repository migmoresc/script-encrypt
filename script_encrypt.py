""" Encripta y desencripta el contenido de los ficheros comunes """

import sys
import os
import base64
from cryptography.fernet import Fernet


def main():
    """ Función principal """
    ayuda = ["-h", "--h", "/h", "-help", "--help", "/help"]
    comandos = ["-e", "-d"]
    html = ["DOCTYPE", "html", "head", "title", "body", "header",
            "main", "nav", "article", "aside", "footer"]
    css = []
    javascript = []
    extensiones = [html, css, javascript]

    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))

    if (len(sys.argv) < 4 or sys.argv[1] in ayuda or sys.argv[1] not in comandos or
            len(sys.argv[3:]) == 0):
        print("""Los argumentos de este script son:
        Primer argumento: -e (encriptar) o -d (desencriptar)
        Segundo argumento: contraseña
        Siguientes argumentos: nombres de los ficheros separados por espacio""")
    else:
        password = str.encode(sys.argv[2]+("0"*(32-len(sys.argv[2]))))
        ficheros = sys.argv[3:]
        password = base64.b64encode(password)
        fernet = Fernet(password)

        procesar_ficheros(ficheros, extensiones, sys.argv[1], fernet)


def procesar_ficheros(ficheros, extensiones, modo, fernet):
    """Encripta los ficheros"""

    for fichero in ficheros:
        fichero = fichero.replace(".\\", "")
        if os.path.exists(fichero):
            if os.path.isfile(fichero):
                if os.stat(fichero).st_size > 0:
                    if modo == "-e":
                        with open("encriptado-"+fichero, "wb") as fichero_nuevo:
                            with open(fichero, "r", encoding="utf-8") as fichero_lectura:
                                encripta(fichero_lectura,
                                         fichero_nuevo, extensiones[0], fernet)
                    else:
                        if "encriptado-" in fichero:
                            fichero_nuevo = fichero.replace(
                                "encriptado-", "desencriptado-")
                        with open(fichero_nuevo, "w", encoding="utf-8") as fichero_nuevo:
                            with open(fichero, "rb") as fichero_lectura:
                                desencripta(fichero_lectura,
                                            fichero_nuevo, extensiones[0], fernet)
                else:
                    print(f'El fichero "{fichero}" está vacío.')
            else:
                print(f'El fichero "{fichero}" no existe. ¿Puede ser que '
                      'hayas introducido el nombre de una carpeta?')
        else:
            print(f'No existe ningún fichero con el nombre "{fichero}".')


def encripta(fichero_lectura, fichero_nuevo, palabras, fernet):
    """ Recorre todas las linea del fichero y lo encripta en el nuevo fichero """
    for linea in fichero_lectura:
        if linea == "\n":
            fichero_nuevo.write(linea.encode("utf-8"))
        else:
            esta = False
            for palabra in palabras:
                if palabra in linea:
                    esta = True
                    break
            if esta is True:
                fichero_nuevo.write(linea.encode("utf-8"))
            else:
                if "\n" in linea:
                    linea = linea[:-1]
                fichero_nuevo.write(fernet.encrypt(linea.encode())+b"\n")


def desencripta(fichero_lectura, fichero_nuevo, palabras, fernet):
    """ Recorre todas las linea del fichero encriptado y lo desencripta en el nuevo fichero """
    for linea in fichero_lectura:
        try:
            if linea == b"\n":
                fichero_nuevo.write(linea.decode("utf-8"))
            else:
                salto = 0
                if b"\n" in linea:
                    linea = linea[:-1]
                    salto = 1
                esta = False
                for palabra in palabras:
                    if palabra.encode() in linea:
                        esta = True
                        break
                if esta is True:
                    fichero_nuevo.write(linea.decode()+"\n"*salto)
                else:
                    fichero_nuevo.write(fernet.decrypt(linea).decode()+"\n")
        except:  # pylint: disable=W0702
            fichero_nuevo.write(fernet.decrypt(linea).decode())


if __name__ == "__main__":
    main()
