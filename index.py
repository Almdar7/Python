# import tkinter as tk
# from tkinter import ttk
# import requests

# def get_causas():
#     url = 'https://localhost:7035/api/Causas/GetCausas'  # Reemplaza 'URL_DEL_ENDPOINT' con la URL real del endpoint

#     try:
#         response = requests.get(url, verify=False)  # Ignoramos la verificación del certificado SSL
#         response.raise_for_status()  # Lanza una excepción si hay un error en la respuesta

#         if response.status_code == 200:
#             # La respuesta es exitosa, parseamos el JSON y lo retornamos
#             return response.json()
#         elif response.status_code == 404:
#             print("No se encontraron datos.")
#             return None
#         else:
#             print(f"Error en la solicitud: {response.status_code} - {response.text}")
#             return None
#     except requests.exceptions.RequestException as e:
#         print(f"Error de conexión: {e}")
#         return None
#     except Exception as ex:
#         raise Exception(f"Se produjo un error al obtener las causas: {ex}")

# def mostrar_datos_en_ventana():
#     data = get_causas()

#     if data is not None:
#         ventana = tk.Tk()
#         ventana.title("Datos de Causas")

#         tabla = ttk.Treeview(ventana, columns=('id_Causa', 'nombreCausa', 'justifica'), show='headings')
#         tabla.heading('id_Causa', text='id_Causa')
#         tabla.heading('nombreCausa', text='nombreCausa')
#         tabla.heading('justifica', text='justifica')

#         tabla.pack()

#         for causa in data:
#             # Asegúrate de que las claves sean las correctas de acuerdo a la estructura del JSON
#             # En este ejemplo, asumimos que el JSON tiene claves 'id', 'nombre', 'descripcion'
#             tabla.insert('', 'end', values=(causa['id_Causa'], causa['nombreCausa'], causa['justifica']))

#         ventana.mainloop()

# mostrar_datos_en_ventana()

# import requests

# def create_repository(repo_name, description, is_private, access_token):
#     api_url = "https://api.github.com/user/repos"
#     headers = {
#         "Authorization": f"token {access_token}"
#     }
#     data = {
#         "name": repo_name,
#         "description": description,
#         "private": is_private
#     }
#     response = requests.post(api_url, headers=headers, json=data)
#     if response.status_code == 201:
#         repository_info = response.json()
#         return repository_info['html_url']
#     else:
#         print(f"Error al crear el repositorio: {response.status_code}")
#         return None


# repo_name = "prueba-python"
# description = "Este es un repo creado para probar la api de github"
# is_private = False  # True si quieres un repositorio privado, False si quieres uno público
# access_token = "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"


# repo_url = create_repository(repo_name, description, is_private, access_token)
# if repo_url:
#     print(f"Repositorio creado: {repo_url}")
# else:
#     print("No se pudo crear el repositorio.")

# import cv2

# def detectar_rostros(frame):
#     cascada_rostros = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#     frame_gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     rostros = cascada_rostros.detectMultiScale(frame_gris, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
#     for (x, y, w, h) in rostros:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
#     return frame

# def capturar_y_mostrar():
#     captura = cv2.VideoCapture(0)
#     while True:
#         ret, frame = captura.read()
#         if ret:
#             # Voltear horizontalmente el frame para quitar el efecto espejo
#             frame = cv2.flip(frame, 1)
            
#             frame_con_rostros = detectar_rostros(frame)
#             cv2.imshow("Deteccion de Rostros", frame_con_rostros)
            
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
    
#     captura.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     capturar_y_mostrar()

# import cv2
# import face_recognition

# def reconocimiento_facial(imagen, nombres_conocidos, encodings_conocidos):
#     # Convertir la imagen a RGB (face_recognition trabaja con imágenes en RGB)
#     imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

#     # Detectar rostros en la imagen
#     rostros = face_recognition.face_locations(imagen_rgb)

#     # Si se detectan rostros, intentar reconocer a las personas
#     for (top, right, bottom, left) in rostros:
#         # Obtener los encodings del rostro detectado
#         rostro_encoding = face_recognition.face_encodings(imagen_rgb, [(top, right, bottom, left)])[0]

#         # Comparar los encodings con los encodings de las personas conocidas
#         coincidencias = face_recognition.compare_faces(encodings_conocidos, rostro_encoding)

#         nombre = "Desconocido"

#         # Verificar si hay alguna coincidencia con las personas conocidas
#         if True in coincidencias:
#             indice = coincidencias.index(True)
#             nombre = nombres_conocidos[indice]

#         # Dibujar un rectángulo y el nombre de la persona en el rostro detectado
#         cv2.rectangle(imagen, (left, top), (right, bottom), (0, 255, 0), 2)
#         cv2.putText(imagen, nombre, (left, top - 20), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 255, 0), 1)

#     return imagen

# # Cargar las imágenes de las personas conocidas y obtener sus encodings
# imagen_yo = face_recognition.load_image_file("dario.jpg")

# encoding_persona = face_recognition.face_encodings(imagen_yo)[0]

# # Lista de encodings y nombres de las personas conocidas
# encodings_conocidos = [encoding_persona]
# nombres_conocidos = ["Dario Rivalta"]



# def reconocimiento_facial_en_video():
#     captura = cv2.VideoCapture(0)

#     while True:
#         ret, frame = captura.read()

#         if ret:
#             # Voltear el marco horizontalmente
#             frame = cv2.flip(frame, 1)
            
#             frame_con_reconocimiento = reconocimiento_facial(frame, nombres_conocidos, encodings_conocidos)
#             cv2.imshow("Reconocimiento Facial", frame_con_reconocimiento)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     captura.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     reconocimiento_facial_en_video()

# import requests
# from bs4 import BeautifulSoup

# def web_scraping(url):
#     # Hacer una solicitud HTTP a la página web
#     response = requests.get(url)
    
#     # Analizar el contenido HTML
#     soup = BeautifulSoup(response.content, 'html.parser')
    
#     # Obtener el título de la página
#     title = soup.title.string
#     print("Título de la página:", title)
    
#     # Obtener el primer párrafo del artículo
#     primer_parrafo = soup.find('p').text
#     print("Primer párrafo:", primer_parrafo)
    
#     # Obtener todos los enlaces en la página
#     enlaces = soup.find_all('a')
#     print("Enlaces:")
#     for enlace in enlaces:
#         print(enlace['href'])

# if __name__ == "__main__":
#     url = 'https://www.mercadolibre.com.ar/'
#     web_scraping(url)


import requests #extracción y manipulación de datos
from bs4 import BeautifulSoup # extracción y manipulación de datos
import tkinter as tk #  crear interfaz
from tkinter import ttk
from PIL import Image, ImageTk #Permite abrir, manipular y guardar imágenes en varios formatos
from io import BytesIO
import re
import base64

def web_scraping(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.string
    paragraphs = soup.find_all('p')[:20]
    images = soup.find_all('img')[12:17]
    data = []

    for paragraph, image_tag in zip(paragraphs, images):
        text = paragraph.get_text()
        image_url = image_tag.get('src') if image_tag else None
        data.append((text, image_url))

    return title, data

def cargar_imagen_desde_url(url):
    response = requests.get(url)
    imagen_bytes = BytesIO(response.content)
    imagen = Image.open(imagen_bytes)
    return imagen

def cargar_imagen_desde_base64(base64_data):
    imagen_bytes = base64.b64decode(base64_data)
    imagen = Image.open(BytesIO(imagen_bytes))
    return imagen

def mostrar_datos_en_ventana(title, data):
    ventana = tk.Tk()
    ventana.title("Presentación - MONSTREITOR 2.0")

    # Personalizar colores y estilos
    bg_color = "#f0f0f0"  # Color de fondo
    text_color = "#333"   # Color de texto
    font = ("Helvetica", 12, "normal")  # Fuente

    ventana.configure(bg=bg_color)
    ventana.geometry("600x1080")  # Tamaño de la ventana

    # Centrar la ventana en la pantalla
    ventana.update_idletasks()
    width = ventana.winfo_width()
    height = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() // 2) - (width // 2)
    y = (ventana.winfo_screenheight() // 2) - (height // 2)
    ventana.geometry(f"{width}x{height}+{x}+{y}")

    frame = ttk.Frame(ventana)
    frame.pack(fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(frame)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    scrollable_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    tk.Label(scrollable_frame, text="MONSTREITOR 2.0", font=("Helvetica", 16, "bold"), fg=text_color, bg=bg_color).pack()
    tk.Label(scrollable_frame, text="", font=font, fg=text_color, bg=bg_color).pack()
    tk.Label(scrollable_frame, text=title, font=font, fg=text_color, bg=bg_color).pack()
    tk.Label(scrollable_frame, text="", font=font, fg=text_color, bg=bg_color).pack()

    for idx, (parrafo, imagen_url) in enumerate(data, start=1):
        # tk.Label(scrollable_frame, text=f"Párrafo {idx}:", font=font, fg=text_color, bg=bg_color).pack()
        tk.Label(scrollable_frame, text=f"", font=font, fg=text_color, bg=bg_color).pack()
        tk.Label(scrollable_frame, text=parrafo, font=font, fg=text_color, bg=bg_color).pack()

        if imagen_url:
            if not imagen_url.startswith('data:image'):
                imagen = cargar_imagen_desde_url(imagen_url)
            else:
                imagen_base64 = re.search(r'base64,(.*)', imagen_url).group(1)
                imagen = cargar_imagen_desde_base64(imagen_base64)

            imagen.thumbnail((200, 200))  
            imagen_tk = ImageTk.PhotoImage(imagen)
            tk.Label(scrollable_frame, image=imagen_tk, bg=bg_color).pack()

            tk.Label(scrollable_frame, image=imagen_tk).image = imagen_tk

    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    ventana.mainloop()

if __name__ == "__main__":
    url = 'https://www.mercadolibre.com.ar/'
    title, data = web_scraping(url)
    mostrar_datos_en_ventana(title, data)










