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
        #Se guardan los objetos de DICOM
        self.archivos = []

    def cargar_archivos(self, ruta_directorio):
        """
        Escanea la carpeta dada, identifica los .dcm y los carga con pydicom.dcmread().
        Maneja errores si algún archivo no es válido.
        """

        #Limpia la lista
        self.archivos = []

        #Verifica que un directorio exista y si no tira error 
        if not os.path.isdir(ruta_directorio):
            raise ValueError(f"La ruta '{ruta_directorio}' no es un directorio válido.")

        #Recorre todos los archivos para identificar los que son DICOM y los que no
        for nombre_archivo in os.listdir(ruta_directorio):

            #Construye una ruta completa
            ruta_completa= os.path.join(ruta_directorio, nombre_archivo)

            #Procesa solo los archivos dentro de la carpeta, no la carpeta
            if not os.path.isfile(ruta_completa):
                continue

            #Intenta leer el archivo como DICOM
            try:
                dcm= pydicom.dcmread(ruta_completa)
                self.archivos.append(dcm)
                print(f"Archivo DICOM Cargado: {nombre_archivo}")

            except Exception as e:
                print(f"'{nombre_archivo}' no es un archivo DICOM válido: {e}")

        print(f"\nTotal DICOM cargados: {len(self.archivos)}")
        return self.archivos
    
    def extraer_metadatos(self, dcm):
        """
        Extrae los campos solicitados de un objeto pydicom.Dataset y devuelve un diccionario con los nombres de columna.
        """
        #Se usa .get() para evitar KeyError si falta el tag
        paciente_ID= dcm.get("PatientID", None)
        nombre_paciente= dcm.get("PatientName", None)
        estudio_ID= dcm.get("StudyInstanceUID", None)
        estudio_desc= dcm.get("StudyDescription", None)
        fecha_estudio= dcm.get("StudyDate", None)
        #Modifica la fecha dada por los archivos DICOM y la organiza con / si cumple el formato
        if fecha_estudio is not None and len(str(fecha_estudio)) == 8:
            fecha_estudio= f"{fecha_estudio[0:4]}/{fecha_estudio[4:6]}/{fecha_estudio[6:8]}"
        modalidad= dcm.get("Modality", None)
        filas= dcm.get("Rows", None)
        columnas= dcm.get("Columns", None)
        
        if hasattr(dcm, "PixelData"):
            #Si el atributo PixelData existe intenta obtener la intensidad promedio
            try:
                imagen= dcm.pixel_array
                intensidad_promedio= np.mean(imagen)
            except Exception as e:
                print("No se pudo leer pixel_array:", e)
                intensidad_promedio= "No hay"
        else:
            intensidad_promedio= "No hay"
            
        if nombre_paciente is not None:
            #Convierte a str los nombres de pacientes 
            try:
                nombre_paciente= str(nombre_paciente)
            except:
                pass
        #Guarda toda la información en un diccionario que use el dataframe
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

        #Reemplaza el none por No hay
        for clave, valor in datos.items():
            if valor is None:
                datos[clave]= "No hay"
    
        return datos
    


    def crear_dataframe_metadatos(self):
        """
        Recorre todos los archivos cargados, extrae metadatos y devuelve un DataFrame de Pandas.
        """
    
        lista_metadatos= []  
        
        #Usa los metadatos extraídos y la lista     
        for dcm in self.archivos:
            meta= self.extraer_metadatos(dcm)
            lista_metadatos.append(meta)
    
        #Crea el DataFrame
        df= pd.DataFrame(lista_metadatos)
    
        return df
    

