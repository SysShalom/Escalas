import os
import tkinter as tk
import tkinter.messagebox as messagebox
import time
import threading
import PyPDF2

# Función que realiza la acción de ajustar
def ajustar():
    # Directorio donde se almacenan los documentos a ajustar
    input_dir = '/ruta/a/tus/documentos'

    # Directorio donde se guardarán los documentos ajustados
    output_dir = '/ruta/a/documentos/listos/para/imprimir'

    # Verifica si el directorio de salida existe, si no, lo crea
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Recorre todos los archivos en el directorio de entrada
    for filename in os.listdir(input_dir):
        if filename.endswith('.pdf'):
            # Abre el documento
            with open(os.path.join(input_dir, filename), 'rb') as file:
                reader = PyPDF2.PdfFileReader(file)
                writer = PyPDF2.PdfFileWriter()

                # Ajusta la escala de cada página
                for page_num in range(reader.getNumPages()):
                    page = reader.getPage(page_num)
                    # Ajusta la escala aquí (esto es solo un ejemplo, necesitarás ajustarlo a tus necesidades)
                    page.scaleBy(0.57)  # Ajusta la escala al 57%
                    writer.addPage(page)

                # Guarda el documento ajustado en el directorio de salida
                with open(os.path.join(output_dir, filename), 'wb') as output_file:
                    writer.write(output_file)

    messagebox.showinfo("Información", "Se han realizado los ajustes necesarios.")
    time.sleep(5)
    root.quit()

# Crea la ventana principal
root = tk.Tk()
root.title("Ajustador de documentos")

# Añade un botón que llama a la función de ajustar cuando se presiona
boton_ajustar = tk.Button(root, text="Ajustar", command=lambda: threading.Thread(target=ajustar).start())
boton_ajustar.pack()

# Añade una etiqueta con tu nombre
nombre = "DEV:Oscar Alvarado"  # Reemplaza esto con tu nombre
etiqueta_nombre = tk.Label(root, text=f"ELABORADO POR:\n{nombre}")
etiqueta_nombre.pack()

# Muestra la ventana
root.mainloop()
