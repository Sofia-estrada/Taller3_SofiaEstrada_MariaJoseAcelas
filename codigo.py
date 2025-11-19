# -*- coding: utf-8 -*-
"""
Created on Sat Nov 15 17:22:38 2025

@author: Sofia
"""

import os
import pydicom
import numpy as np 
import pandas as pd 

class ProcesadorDICOM:
    def __init__(self):
        # aquí guardaremos los objetos DICOM cargados
        self.archivos = []

    def cargar_archivos(self, ruta_directorio):
        """
        Escanea la carpeta dada, identifica los .dcm y los carga con pydicom.dcmread().
        Maneja errores si algún archivo no es válido.
        """

        # Limpiar lista por si se llama dos veces
        self.archivos = []

        # Verificar que el directorio exista
        if not os.path.isdir(ruta_directorio):
            raise ValueError(f"La ruta '{ruta_directorio}' no es un directorio válido.")

        # Recorrer todos los archivos dentro del directorio
        for nombre_archivo in os.listdir(ruta_directorio):

            # Construir la ruta completa
            ruta_completa = os.path.join(ruta_directorio, nombre_archivo)

            # Solo procesar archivos (ignorar carpetas)
            if not os.path.isfile(ruta_completa):
                continue

            # Intentar leer el archivo como DICOM
            try:
                dcm = pydicom.dcmread(ruta_completa)
                self.archivos.append(dcm)
                print(f"Archivo DICOM Cargado: {nombre_archivo}")

            except Exception as e:
                print(f"'{nombre_archivo}' no es un archivo DICOM válido: {e}")

        print(f"\nTotal DICOM cargados: {len(self.archivos)}")
        return self.archivos
    
    def extraer_metadatos(self, dcm):
        """
        Extrae los campos solicitados de un objeto pydicom.Dataset.
        Devuelve un diccionario con los nombres de columna.
        """
        # Usar .get() para evitar KeyError si falta el tag
        paciente_ID= dcm.get("PatientID", None)
        nombre_paciente= dcm.get("PatientName", None)
        estudio_ID= dcm.get("StudyInstanceUID", None)
        estudio_desc= dcm.get("StudyDescription", None)
        fecha_estudio= dcm.get("StudyDate", None)
        modalidad= dcm.get("Modality", None)
        filas= dcm.get("Rows", None)
        columnas= dcm.get("Columns", None)
        
        if hasattr(dcm, "PixelData"):
            try:
                imagen = dcm.pixel_array
                intensidad_promedio = np.mean(imagen)
            except Exception as e:
                print("No se pudo leer pixel_array:", e)
                intensidad_promedio = "NA"
        else:
            intensidad_promedio = "NA"
            
        if nombre_paciente is not None:
            try:
                nombre_paciente= str(nombre_paciente)
            except:
                pass
        
        datos= {
        "ID paciente": paciente_ID,
        "Nombre paciente": nombre_paciente,
        "Identificador único de estudio": estudio_ID,
        "Descripcion del estudio": estudio_desc,
        "Fecha del estudio": fecha_estudio,
        "Modalidad imagen": modalidad,
        "# Filas": filas,
        "# Columnas": columnas,
        "Intensidad promedio":intensidad_promedio
        }

        # Reemplazar automáticamente None por "NA"
        for clave, valor in datos.items():
            if valor is None:
                datos[clave] = "NA"
    
        return datos
    


    def crear_dataframe_metadatos(self):
        """
        Recorre todos los archivos cargados, extrae metadatos
        y devuelve un DataFrame de Pandas.
        """
    
        lista_metadatos = []  # Aquí guardaremos cada diccionario
    
        for dcm in self.archivos:
            meta = self.extraer_metadatos(dcm)
            lista_metadatos.append(meta)
    
        # Crear el DataFrame
        df = pd.DataFrame(lista_metadatos)
    
        return df
    

