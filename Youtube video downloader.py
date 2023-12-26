#Importamos la librería
import yt_dlp
import os
import sys 

#Ruta para encontrar la carpeta de descarga del usuario 
ruta_de_descarga = os.path.expanduser("~") + "/Downloads/"

#Función que se usa para consegur el enlace del que se descargará el video 
def conseguir_enlace():
	if len(sys.argv) == 3: 
		url = sys.argv[1]
		print(url)
	else: 
		print("Por favor, ingrese un enlace valido")
		url = None

	return url 

#Función para seleccionar la calidad de descarga 
def seleccionar_calidad():
		if len(sys.argv) == 3: 
			option = int(sys.argv[2])
			print(option)
			if(option == 1): 
				yt_opts = {"format": "(mp4,webm)[height<=1080]",
						'outtmpl': f'{ruta_de_descarga}%(title)s.%(ext)s'} 
			elif(option == 2): 
				yt_opts = {"format": "(mp4,webm)[height<=720]",
						'outtmpl': f'{ruta_de_descarga}%(title)s.%(ext)s'} 
			elif (option == 3): 
				yt_opts = {"format": "(mp4,webm)[height<=480]",
						'outtmpl': f'{ruta_de_descarga}%(title)s.%(ext)s'} 
			elif (option == 4): 
				yt_opts = {"format": "(mp4,webm)[height<=360]",
						'outtmpl': f'{ruta_de_descarga}%(title)s.%(ext)s'} 
			elif (option == 5): 
				yt_opts = {"format": "(mp4,webm)[height<=180]",
						'outtmpl': f'{ruta_de_descarga}%(title)s.%(ext)s'} 
			elif (option == 6): 
				yt_opts = {'outtmpl': f'{ruta_de_descarga}%(title)s.%(ext)s'}
		else: 
			print("Por favor, ingrese una opción valida")
			yt_opts = None
		
		return yt_opts

#Función que se usa para generar la descarga del video con la 
def generar_descgarga():
	with yt_dlp.YoutubeDL(seleccionar_calidad()) as ydl:
		ydl.download([conseguir_enlace()])

#Mandamos llamar la función con manejo de error por si el usuario no 
try: 
	generar_descgarga()
except:
	print(ValueError("No se cuenta con los parámetros completos"))