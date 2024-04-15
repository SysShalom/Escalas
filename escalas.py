import os
import PyPDF2

# Función que realiza la acción de ajustar
def ajustar():
    # Directorio donde se almacenan los documentos a ajustar
    # Reemplazar esta ruta con la ruta de directorios del ordenador
    input_dir = r'C:\Users\oscar\OneDrive\Escritorio\RP80 Series(202308)-CD'

    # Directorio donde se guardarán los documentos ajustados
    # Reemplaza esto con la ruta a tu carpeta de salida
    output_dir = r'C:\Users\oscar\OneDrive\Escritorio\RP80 Series(202308)-CD\DocumentosAjustados'

    # Verifica si el directorio de salida existe, si no, lo crea
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Recorre todos los archivos en el directorio de entrada
    for filename in os.listdir(input_dir):
        # Solo procesa archivos que terminen en '.pdf'
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

    # Imprime un mensaje en la consola cuando se han realizado los ajustes
    print("Se han realizado los ajustes necesarios.")

# Llama a la función de ajustar
ajustar()
