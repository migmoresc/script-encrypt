# script-encrypt
Script para encriptar archivos


¿Cómo se usa?

Desde la terminal escribiremos para encriptar los archivos:

	python script-encrypt.py -e micontraseña nombreArchivo1.html nombreArchivo2.html ...

Y para desencriptar:

	python script-encrypt.py -d micontraseña nombreArchivo1.html nombreArchivo2.html ...



No acepto pull request / I don't accept pull request


CHANGELOG


Versión 1.1

	Código refactorizado
	Añadido main

Versión 1.0

	Programa que funciona y sólo encripta html

TO DO

- Encriptar según la extensión del archivo.
- Añadir la lógica para otras extensiones como css, js ...
- Añadir la opción de usar un fichero que contenga los nombre de los archivos.